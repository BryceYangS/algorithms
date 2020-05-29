# 블랙잭
# import itertools
#
# userInput = list(map(int, input().split(" ")))
# cardNums = list(map(int, input().split(" ")))
#
# rtn = 0
# minusVal = 0
#
# combList = list(itertools.combinations(cardNums,3))
#
# for comb in combList:
#     sumComb = sum(comb)
#     # 목표값 - 뽑은 카드 합
#     minus = userInput[1] - sumComb
#     if minus == 0:
#         rtn = sumComb
#         break
#     elif minus < 0:
#     # 목표값 < 뽑은 카드 합
#         continue
#     else:
#     # 목표값 > 뽑은 카드 합
#         if minusVal == 0:
#             minusVal = minus
#             rtn = sumComb
#         elif minusVal > minus:
#             minusVal = minus
#             rtn = sumComb
# print(rtn)


# 블랙잭 풀이 ( 완전 탐색 )

n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sumVal = data[i] + data[j] + data[k]
            if sumVal <= m:
                result = max(sumVal, result)
print(result)

