# python practice
# Question 4: Dictionary Normalization

# You receive inconsistent user data.

# Task:

# Implement a class UserDataCleaner with:

# __init__(self, data_dict)
# clean_data(self):
# Remove keys with None values
# Convert all string values to lowercase
# Trim spaces

# Input: {"Name": "  JOHN ", "age": None}
# Output: {"Name": "john"}

class UserDataCleaner():
    def __init__(self,data_dict):
        self.data_dict = data_dict

    def clean_data(self):
        d = {}
        for key,value in self.data_dict.items():
            if self.data_dict[key] is not None:
                if isinstance(value,str):
                    d[key] = value.lower().strip()
                else:
                    d[key] = value
        
        return d

print(UserDataCleaner({"Name": "  JOHN ", "age": None}).clean_data())