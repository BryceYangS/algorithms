
import sys

n = int(input())
cranes = list(map(int,input().split()))

m = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
count = 0
for box in range(count, len(boxes)):

    for crane in cranes:
        if box <= crane:
            count += 1
            break
