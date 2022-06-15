from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    fact1 = k % len(nums)
    print("value of fact1", fact1)
    
    nums[:] = nums[-fact1 : ] + nums[:-fact1]

nums = [1,2,3,4,5,6,7]
k = 4

rotate(nums, k)
print("After Rotation", nums)