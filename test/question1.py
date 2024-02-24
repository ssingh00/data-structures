from collections import defaultdict
def solution(S):
    # Implement your solution here
    count = defaultdict(int)
    palindrome = mid = ''
    for i in S:
        count[i] += 1

	for d in sorted(count.keys(), reverse=True):        
        mid = max(mid, d * (count[d] & 1))
        palindrome += d * (count[d] // 2)

	palindrome = palindrome.lstrip('0')
	return (palindrome + mid + palindrome[::-1]) or '0'
    

print(solution("39878"))
print(solution("00900"))