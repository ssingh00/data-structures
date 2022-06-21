def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if (x<0):
        return False
    i = x
    s = 0
    while(i > 0):
        d = i % 10
        print(">", d)
        s = s * 10 + d  
        print(">>>", s)
        i = int(i / 10)
        print(">>>>>", i)
    if (x == s):
        return True
    return False

result  = isPalindrome(12321)
print(result)