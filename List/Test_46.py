# Question 1: String Normalization & Validation

# You are developing a system that validates user-entered product codes.

# A valid product code:

# Should ignore spaces and dashes (-)
# Must contain only alphanumeric characters after cleaning
# Must have at least 2 letters and 2 digits
import re
class ProductCodeValidator():
    def __init__(self,str):
        self.str = str
    def is_valid(self):
        res = re.sub(r"[^a-zA-Z0-9]","",self.str)
        cnt = 0
        cnt1 = 0
        for i in res:
            if i.isdigit():
                cnt+=1
            else:
                cnt1+=1
        return cnt >= 2 and cnt1 >= 2

print(ProductCodeValidator("abcd").is_valid())