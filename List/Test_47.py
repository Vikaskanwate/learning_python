# Question 2: Custom Frequency Filter

# You are analyzing logs and want to filter characters based on frequency.

# Task:

# Implement a class CharFrequencyFilter with:

# __init__(self, text)
# filter_chars(self, k) → return characters that appear exactly k times

class CharFrequencyFilter():
    def __init__(self,text):
        self.text = text
    def filter_chars(self,k):
        freq = {}
        for ch in self.text:
            freq[ch] = freq.get(ch,0)+1
        result = []
        for ch in self.text:
            if freq[ch] == k and ch not in result:
                result.append(ch)
        # return [ch for ch in freq if freq[ch] == 2]
        return result
print(CharFrequencyFilter("aabbccc").filter_chars(2))
