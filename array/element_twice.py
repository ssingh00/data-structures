from typing import List 
def containsDuplicate(nums: List[int]) -> bool:
    return not len(set(nums)) == len(nums)
    
nums = [1,2,3,4]
print(containsDuplicate(nums))