'''
[수 정렬하기 3]
https://www.acmicpc.net/problem/10989
'''

'''
10
5
2
3
1
4
2
3
5
1
7
'''
import sys

n = int(sys.stdin.readline())
arr_cnt = [0] * 10001

for _ in range(n):
    arr_cnt[int(sys.stdin.readline())] += 1

for i in range(len(arr_cnt)):
    if arr_cnt[i] > 0:
        for _ in range(arr_cnt[i]):
            print(i)

# for index in range(len(arr) - 1):
#     swap = False
#     for index2 in range(len(arr) - index - 1):
#         if arr[index2] > arr[index2 + 1]:
#             arr[index2], arr[index2 + 1] = arr[index2 + 1], arr[index2]
#             swap = True
#
#     # 한번도 스왑되지 않으면 이미 정렬 되어 있음
#     if swap == False:
#         break;
#
# for i in range(len(arr)):
#     print(arr[i])


'''
문제풀이 핵심 아이디어
    1. 데이터 개수가 최대 10,000,000개 : 파이썬의 경우 일반 정렬 알고리즘 사용 시 메모리 사용 초과 에러 발생
    2. 시간 복잡도 O(N)의 정렬 알고리즘 이용해야 함
    3. 수의 범위가 1 ~ 10,000이므로 계수 정렬 이용 가능 
'''

# 계수 정렬(Counting Sort) 알고리즘
#   - 수의 범위 제한이 있을 경우 사용 가능
#   - 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
#   - 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
#   - 데이터가 등장한 횟수를 센다

# ►유의사항◀︎
# 데이터 개수가 많을 때 파이썬에서는 input()대신 sys.stdin.readline()을 사용해야 함

