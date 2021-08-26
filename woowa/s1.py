def solution(U, L, C):
    # write your code in Python 3.6

    if U + L != sum(C):
        return 'IMPOSSIBLE'

    arrLength = len(C)
    firstRow = [0 for i in range(arrLength)]
    secondRow = [0 for i in range(arrLength)]

    for i in range(arrLength):
        if C[i] == 2:
            firstRow[i] = 1
            secondRow[i] = 1
        elif C[i] == 0:
            firstRow[i] = 0
            secondRow[i] = 0
        else:
            if sum(firstRow) < U:
                firstRow[i] = 1
                secondRow[i] = 0
                continue
            firstRow[i] = 0
            secondRow[i] = 1

    return ''.join(str(x) for x in firstRow) + ',' + ''.join(str(x) for x in secondRow)


print(solution(3, 2, [2, 1, 1, 0, 1]))
print(solution(2, 3, [0, 0, 1, 1, 2]))
