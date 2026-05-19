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
        # digits = 0
        # letters = 0
        # for i in res:
        #     if i.isdigit():
        #         digits+=1
        #     else:
        #         letters+=1
        digits = sum(ch.isdigit() for ch in res)
        letters = sum(ch.isalpha() for ch in res)

        return digits >= 2 and letters >= 2

print(ProductCodeValidator("abcd").is_valid())