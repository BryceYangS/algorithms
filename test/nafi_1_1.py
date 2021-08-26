# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, S):
    # write your code in Python 3.6

    totalP = sum(P)
    useCarNum = 0
    S.sort(reverse=True)

    for i in range(len(S)):
        totalP -= S[i]
        useCarNum += 1
        if totalP <= 0:
            break

    return useCarNum


# print(solution([1, 4, 1], [1, 5, 1]))
# print(solution([4, 4, 2, 4], [5, 5, 2, 5]))
# print(solution([2, 3, 4, 2], [2, 5, 7, 2]))
# print(solution([9, 9, 9, 9], [9, 9, 9, 9]))
# print(solution([9, 9, 9, 9, 1, 1], [9, 9, 9, 9, 2, 3]))
print(solution([1,2,3,4], [9,2,3,4]))

