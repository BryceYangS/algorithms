def solution(A):
    # write your code in Python 3.6
    A.sort()

    for a in A:
        if a >= 0:
            return 0
        if -a in A:
            return -a
    return 0


print(solution([3, 2, -2, 5, -3]))
print(solution([1,2,0,0,-1,-2]))
print(solution([1,2,0,0,-1,-2]))
print(solution([1,1,1,1,1,-1]))
print(solution([1,1,1,1,1,-1, -2,2]))