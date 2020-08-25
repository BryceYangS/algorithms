'''
[좌표정렬하기]
https://www.acmicpc.net/problem/11650

2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''


'''
input====
5
3 4
1 1
1 -1
2 2
3 3
output===
5
3 4
1 1
1 -1
2 2
3 3
'''
n = (int)(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split(' '))
    arr.append((x, y))

# arr = sorted(arr, key=lambda x: (x[0], x[1]))
arr = sorted(arr)

for i in arr:
    print(i[0], i[1])

