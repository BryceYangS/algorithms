
'''
7
1 6
1 7
3 2
3 1
2 4
2 5
6 1
'''
import heapq

n = int(input())
array = []
q = []

# 문제 정보를 입력 받은 이후에, 데드라인을 기준으로 정렬
for _ in range(n):
    array.append(tuple(map(int,input().split(' '))))
array.sort()

for i in array:
    a = i[0]
    heapq.heappush(q, i[1])
    # 데드라인을 초과하는 경우 최소 원소를 제거
    if a < len(q):
        heapq.heappop(q)

print(sum(q))