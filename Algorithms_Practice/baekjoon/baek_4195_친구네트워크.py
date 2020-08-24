'''
https://www.acmicpc.net/problem/4195
'''



def solution(relation_arr):
    relation_arr
    output = []
    count = 0
    for i in range(len(relation_arr)):
        if i == 0:
            count = len(relation_arr[i])
            output.append(count)
            continue
        for j in range(0, i):
            if relation_arr[i][0] == relation_arr[j][1]:
                count += 1
                for k in range(0,i):
                    if relation_arr[i][1] == relation_arr[k][0]:
                        count += 1
                        break
                break
        output.append(count)

    return output


test_case = (int)(input())
print_arr = []
relation_arr = []
for i in range(test_case):
    relation_cnt = (int)(input())
    tmp_arr = []
    for j in range(relation_cnt):
        tmp_arr.append(tuple(map(str, input().split())))

    relation_arr.append(tmp_arr)

for i in range(test_case):
    print_arr.extend(solution(relation_arr[i]))

for  a in print_arr:
    print(a)

'''
Input 
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty

Ouput
2
3
4
2
2
4

'''


'''
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