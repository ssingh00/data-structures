from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('inf'), float('-inf')
        for price in prices:
            cost = min(cost, price)
            profit= max(price - cost, profit)

        return profit

if __name__ == '__main__':
    sl = Solution()
    prices = [7,1,5,3,6,4]
    print(sl.maxProfit(prices))
    prices = [7,6,4,3,1]
    print(sl.maxProfit(prices))
    prices =  [3,3]
    print(sl.maxProfit(prices))
    prices = [2,4,1]
    print(sl.maxProfit(prices))