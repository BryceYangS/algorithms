'''
https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
'''
from decimal import Decimal
def solution(lines):
    answer = 1

    tmp = [(
        (int)(i.split(' ')[1].split(':')[0]) * 3600 + (int)(i.split(' ')[1].split(':')[1]) * 60 + Decimal(
            i.split(' ')[1].split(':')[2]) + Decimal('0.001') - Decimal(i.split(' ')[2][:-1]),
        (int)(i.split(' ')[1].split(':')[0]) * 3600 + (int)(i.split(' ')[1].split(':')[1]) * 60 + Decimal(
            i.split(' ')[1].split(':')[2])
    ) for i in lines]  # (start, end)
    # print(tmp)

    #     for log1 in tmp:
    #         chkSt = log1[0] - Decimal('0.0001')
    #         chkEd = log1[0] + 1
    #         # chkSt = log1[0]
    #         # chkEd = log1[0] + Decimal('0.9999')

    #         maxProcess = 0
    #         for log2 in tmp:
    #             if log2[0] < chkEd and log2[1] > chkSt:
    #                 maxProcess += 1
    #             # elif chkSt < log2[1] < chkEd:
    #             #     maxProcess += 1
    #         answer = maxProcess if answer < maxProcess else answer
    #     print(answer)

    for log1 in tmp:
        chkSt = log1[1] - Decimal('0.001')
        chkEd = log1[1] + 1

        maxProcess = 0
        for log2 in tmp:
            if log2[0] < chkEd and log2[1] > chkSt:
                maxProcess += 1

        answer = maxProcess if answer < maxProcess else answer

    return answer

# solution([
# '2016-09-15 01:00:04.001 2.0s',
# '2016-09-15 01:00:07.000 2s'])


# solution(["2016-09-15 00:00:00.000 3s"])
# solution(["2016-09-15 23:59:59.999 0.001s"])
solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
# solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
# solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
# solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"])