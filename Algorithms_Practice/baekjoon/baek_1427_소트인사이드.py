'''
[소트인사이드]
https://www.acmicpc.net/problem/1427
'''

'''
# 내 답안
n = list(map(int, list(input())))
n.sort(reverse=True)

print("".join(map(str, n)))
'''


# 다른 답안

array = input()
for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')
