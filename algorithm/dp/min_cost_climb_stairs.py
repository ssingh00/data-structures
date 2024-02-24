from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. A function that returns the answer
        def dp(i):
            if i <= 1:
                # 3. Base cases
                return 0
            
            if i in memo:
                return memo[i]
            
            # 2. Recurrence relation
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))
    
if __name__=="__main__":
    sl = Solution()
    print(sl.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))