# find pair of sum
def pair_sum(nums,target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen[num] = True
        print(seen)
    return False
print(pair_sum([2, 7, 11, 15],9))