from fastapi import FastAPI,UploadFile,File,HTTPException,status
from pydantic import BaseModel
from typing import List, Optional
import javalang

app = FastAPI(
    title="CodeContext Parser API",
    description="Extracts structural metadata from Java source files.",
    version="1.0.0"
)

class MethodModel(BaseModel):
    name:str
    return_type:str
    modifiers:List[str]

class ClassModel(BaseModel):
    name:str
    modifiers:List[str]
    extends:Optional[str] = None

class CodeStructureResponse(BaseModel):
    classes : List[ClassModel]
    methods : List[MethodModel]


def parse_java_code(source_code: str) -> dict:
    try:
        # Parse code into an Abstract Syntax Tree (AST)
        tree = javalang.parse.parse(source_code)
        
        extracted_classes = []
        extracted_methods = []
        
        # Walk through the AST to find Class Declarations
        for path, node in tree.filter(javalang.tree.ClassDeclaration):
            extends_name = node.extends.name if node.extends else None
            extracted_classes.append(ClassModel(
                name=node.name,
                modifiers=list(node.modifiers),
                extends=extends_name
            ))
            
        # Walk through the AST to find Method Declarations
        for path, node in tree.filter(javalang.tree.MethodDeclaration):
            # Safe extraction of the return type string
            ret_type = "void"
            if node.return_type:
                ret_type = getattr(node.return_type, 'name', str(node.return_type))
                
            extracted_methods.append(MethodModel(
                name=node.name,
                return_type=ret_type,
                modifiers=list(node.modifiers)
            ))
            
        return {
            "classes": extracted_classes,
            "methods": extracted_methods
        }
        
    except javalang.parser.JavaSyntaxError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid Java Syntax: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Parser Error: {str(e)}"
        )
    
@app.post("/api/v1/parse-java", response_model=CodeStructureResponse, tags=["Parser"])
async def upload_java_file(file: UploadFile = File(...)):
    """
    Accepts a .java file upload and outputs structural metadata in JSON format.
    """
    # Validation check for file extension
    if not file.filename.endswith('.java'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only valid .java source files are accepted."
        )
        
    # Read file content safely
    contents = await file.read()
    source_code = contents.decode("utf-8")
    
    return parse_java_code(source_code)