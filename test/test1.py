# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    A = list(set(A))
    A.sort()

    if A[-1] < 0:
        return 1

    for i in range(len(A) - 1):
        if (A[i] + 1) != A[i + 1]:
            if A[i] + 1 > 0:
                return A[i] + 1

    return A[-1] + 1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
print(solution([-89, -3, -47, -5, -2, -1, 1]))
