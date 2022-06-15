import sys
from typing import List

def maxSubArray(nums: List[int]) -> int:
    global_max = -sys.maxsize
    print("global_max", global_max)
    size = len(nums)
    local_max = 0
    
    for i in range(size):
        local_max = max(nums[i], nums[i] + local_max)
        print(local_max)
        if local_max > global_max:
            global_max = local_max
            print("global_max >>>> ", local_max)
    
    return global_max

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
