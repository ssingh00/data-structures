from typing import List

def plusOne(digits: List[int]) -> List[int]:
    val1 = enumerate(digits)
    val = [*enumerate(digits)]
    val2 = [*enumerate(digits)][::-1]
    for i, num in [*enumerate(digits)][::-1]:
        if num != 9:
            digits[i] += 1
            break
        digits[i] = 0
    print(digits)
    print([1] + digits )
    print([1] + digits if not digits[0] else digits)
# def plusOne(digits: List[int]) -> List[int]:
#     last_index= len(digits)-1
#     def calc(d, i):
#         last_digit = d[i]
#         if d == [9]:
#             return [1, 0]
#         elif last_digit < 9:
#             d[i] = last_digit + 1
#         else:
#             d[i]=0
#             i-=1
#             d = calc(d, i)
#         return d
#     digits = calc(digits, last_index)
#     print(digits)
plusOne([1,2,3])
plusOne([4,3,2,1])
plusOne([9])
plusOne([1, 9])
plusOne([9, 9])