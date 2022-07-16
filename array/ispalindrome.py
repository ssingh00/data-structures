class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        i = x
        s = 0
        while(i > 0):
            r = i % 10
            s = s * 10 + r  
            i = int(i / 10)
        if (x == s):
            return True
        return False
if __name__=="__main__":
    sl = Solution()
    x = 121
    print(sl.isPalindrome(x))
    x = -121
    print(sl.isPalindrome(x))