from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i=0
    temp=0
    while i < len(nums):
        if len(nums)==0:
            return
        if nums[i] == val:
            temp = i
            del nums[i]
            i=temp
        else:
            i+=1

# nums = [0,1,2,2,3,0,4,2]
val = 2
# removeElement(nums, val)

removeElement([2,2,2], 2)