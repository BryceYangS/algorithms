# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    one_len_arr = []

    for i in range(len(A)):
        if A[i] < 0:
            if A[i] * - 1 < 10:
                one_len_arr.append(A[i])
        elif A[i] < 10:
            one_len_arr.append(A[i])

    return max(one_len_arr)


print(solution([-6, -91, 1101, 84, -22, 0, 1, 473]))
print(solution([1, 23, 4, -6, 8, 9, 10, 0, 2341]))
print(solution([-1, -2, -3, -78]))
print(solution([0, 1, 99, 9]))
