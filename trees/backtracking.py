from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return

            ans.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for num in range(i, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()
        
        ans = []
        backtrack([], 1)
        return ans
    
if __name__=="__main__":
    sl = Solution()
    print(sl.permute(nums = [1,2,3]))
    print(sl.subsets(nums = [1,2,3]))
    print(sl.combine(n = 4, k = 2))