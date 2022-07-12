class Solution:
    def mySqrt(self, x: int) -> int:
        low=1
        high=x
        res=0
        while(low<=high):
            mid=int(low+(high-low)//2)
            if mid*mid==x:
                res=mid
                return res
            elif mid*mid<x:
                res=mid
                low=mid+1
            else:
                high=mid-1
            
        return res

if __name__=='__main__':
    sl = Solution()
    n  =  8
    print(sl.mySqrt(n))