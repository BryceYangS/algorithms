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

for i in range(n):
    array.append(tuple(map(int, input().split(' '))))
array.sort()


for i in array:
    dead = i[0]
    heapq.heappush(q, i[1])
    if len(q) > dead:
        heapq.heappop(q)

print(sum(q))
