class Solution:
    def isPalindrome(self, s: str) -> bool:
        empty = []
        s = [char.lower() for char in s if char.isalpha()]
        mid = int(len(s)/2)
        if len(s) % 2 != 0:
            new = s[mid-1::-1]
        else:
            new = s[mid::-1]
        if ''.join(new[::-1]) == ''.join(s[:mid:]):
            return True
        elif (len(s) == 0) or (len(s) == 1):
            return True
        else:
            return False

if __name__ == '__main__':
    sl = Solution()
    s = "a"
    print(sl.isPalindrome(s))
    s = "A man, a plan, a canal: Panama"
    print(sl.isPalindrome(s))
    s = "race a car"
    print(sl.isPalindrome(s))
    s = " "
    print(sl.isPalindrome(s))