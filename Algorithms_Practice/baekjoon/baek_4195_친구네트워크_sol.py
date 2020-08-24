'''
https://www.acmicpc.net/problem/4195

풀이

1. 해시를 활용한 Union-Find 알고리즘 이용해 풀이 가능
2. Python의 경우 dictionary 자료형을 해시처럼 사용 가능

※ Union-Find 알고리즘?
 - 합집합 찾기
 - 원소들의 연결 여부를 확인하는 알고리즘
'''


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])
