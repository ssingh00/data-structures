from typing import List
def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i+=1
                continue
            else:
                return i 
        return i

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 4))