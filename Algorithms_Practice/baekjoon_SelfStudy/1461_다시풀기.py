'''
7 2
-37 2 -6 -39 -29 11 -28

'''
import heapq

book, sej = map(int, input().split(' '))
position = list(map(int, input().split(' ')))

mostFar = max(max(position), -min(position))

result = 0
negative = []
positive = []

# Max heap생성 : 최대값부터 처리해야 하기 때문에 (Python의 heapq는 Min heap이기 때문에 양수값에 -1 곱해줌)
for i in range(len(position)):
    # 음수일 때
    if position[i] < 0:
        heapq.heappush(negative, position[i])
    # 양수일 때
    else:
        heapq.heappush(positive, -position[i])


while negative:
    result += heapq.heappop(negative)
    for _ in range(sej - 1):
        if negative:
            heapq.heappop(negative)

while positive:
    result += heapq.heappop(positive)
    for _ in range(sej - 1):
        if positive:
            heapq.heappop(positive)


print(-result * 2 - mostFar)
