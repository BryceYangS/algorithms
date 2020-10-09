'''
6
10 20 10 30 20 50
'''

n = int(input())
inArr = list(map(int, input().split(' ')))
arr = [[1] * n] * n

for i in range(0, n):
    for j in range(i + 1, n):
        if inArr[i] < inArr[j]:
            tmp = arr[i-1][j-i] + 1
            arr[i][j] = tmp if arr[i][j] < tmp else arr[i][j]


print(arr)