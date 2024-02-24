def solution(S):
    # Implement your solution here
    stack = []
    arr = S.split(" ")    
    for i in range(len(arr)):
        try: 
            if int(arr[i]):
                stack.append(arr[i])
        except:
            if i == "POP":
                stack.pop()
            elif i == "DUP":
                stack.append(stack[-1])
            elif i == "+":
                d1 = stack.pop()
                d2 = stack.pop()
                stack.append(d2 + d2)
            elif i == "-":
                d3 = stack.pop()
                d4 = stack.pop()
                stack.append(d3-d4)
    return stack[-1]


print(solution('4 5 6 - 7 +'))