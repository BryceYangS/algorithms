'''

3
6 8 9
5
2 5 2 4 7

'''


import sys


cranes_cnt = int(input())
cranes = list(map(int, input().split()))

boxes_cnt = int(input())
boxes = list(map(int, input().split()))


if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

cranes.sort(reverse=True)
boxes.sort(reverse=True)

position = [0] * cranes_cnt
check = [False] * boxes_cnt

result = 0
count = 0


while True:
    if count == boxes_cnt:
        break

    for i in range(cranes_cnt):
        while position[i] < boxes_cnt:
            if not check[position[i]] and cranes[i] >= boxes[position[i]]:
                check[position[i]] = True
                position[i] += 1
                count += 1
                break
            position[i] += 1
    result += 1

print(result)
