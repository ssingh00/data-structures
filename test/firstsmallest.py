def solution(A):
    # Implement your solution here
    i = 1
    while i < len(A):
        if i in A:
            i+=1
            continue
        else:
            return i
    return i+1

if __name__=="__main__":
    print(solution([1, 3, 6, 4, 1, 2]))
    print(solution([-1, -3]))
    print(solution([1, 2, 3]))