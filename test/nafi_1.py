# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, S):
    # write your code in Python 3.6

    # canSeatNumber = []
    fullCar = []
    isUseCar = len(P)
    # isNeedChange = False

    남는자리 = 0

    for i in range(len(P)):
        if S[i] - P[i] > 0:
            # canSeatNumber.append((i, S[i] - P[i]))
            남는자리 += S[i] - P[i]
            # isNeedChange = True
        else:
            fullCar.append(i)

    for carIdx in fullCar:
        if 남는자리 - P[carIdx] >= 0:
            남는자리 -= P[carIdx]
            isUseCar -= 1

    return isUseCar


# print(solution([1, 4, 1], [1, 5, 1]))
# print(solution([4, 4, 2, 4], [5, 5, 2, 5]))
# print(solution([2, 3, 4, 2], [2, 5, 7, 2]))
# print(solution([9, 9, 9, 9], [9, 9, 9, 9]))
print(solution([9, 9, 9, 9, 1, 1], [9, 9, 9, 9, 2, 3]))
