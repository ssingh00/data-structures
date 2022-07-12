class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst  = s.split(" ")
        i = len(lst)-1
        while i >= 0:
            if lst[i] == "":
                print(lst[i])
                i-=1
            else:
                return len(lst[i])

if __name__=="__main__":
    sl = Solution()
    s = "a"
    print(sl.lengthOfLastWord(s))