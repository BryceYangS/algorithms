'''
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다.
셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다.
넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.
'''

# 3
# 6 8 9
# 5
# 2 5 2 4 7

'''
 - 매 분마다, 모든 크레인에 대해 옮길 수 있는 박스를 선택해 옮기도록 함
 - 박스를 무게 기준으로 내림차순으로 정렬한 뒤, 무거운 것부터 옮기도록 하면 됨
 - 시간 복잡도 O(NM) 문제 해결 : 크레인 * 박스
'''
import sys

n = int(input())
cranes = list(map(int,input().split()))

m = int(input())
boxes = list(map(int, input().split()))

# 모든 박스를 옮길 수 없는 경우
if max(boxes) > max(cranes):
    print(-1)
    sys.exit()

# 각 크레인이 현재 옮겨야 하는 박스의 번호 (0부터 시작)
positions = [0] * n
checked = [False] * m

# 최적의 해를 구해야 하므로, 내림차순 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
count = 0

while True: # 매 분으로 보면 됨
    if count == len(boxes): #박스를 다 옮겼다면 종료
        break
    for i in range(n) : # 모든 크레인에 대하여 각각 처리
        while positions[i] < len(boxes):
            # 아직 안 옮긴 박스 중에서 옮길 수 있는 박스를 만날 때까지 반복
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)


