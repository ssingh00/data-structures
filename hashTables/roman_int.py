def romanToInt(s: str) -> int:
    dict1 = {'I':1, 'V':5, 'X':10, 'X':10, 'L': 50,'C':100,'D':500,'M':1000}
    val = 0
    temp = ''
    for i in s[::-1]:
        if temp and (dict1[i] < dict1[temp]):
            val = val - dict1[i]
        else:
            val = val + dict1[i]
        print(val)
        temp = i
    return val


print(romanToInt("LVIII"))

print(romanToInt("MCMXCIV"))