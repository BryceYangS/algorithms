'''
- 최대 K개의 집중국을 설치해야 합니다
- 집중국들의 수신 가능 영역의 길이의 합을 최소화하는 것이 목표
- 사실상 정렬만 수행하면 되므로 O(NlogN)으로 문제 해결 할 수 있음
'''


'''
정렬된 센서들 최대 K개의 영역으로 나누는 것과 동일!!!
 - 각 센서를 오름차순 정렬
 - 각 센서 사이의 거리 계산
 - 가장 거리가 먼 순서대로 K - 1 개의 연결고리를 제거
'''

import sys

n = int(input())
k = int(input())

# 집중국의 개수가 n 이상일 때
if k >= n:
    print(0) # 각 센서의 위치에 설치하면 되므로 정답은 0
    sys.exit()

#모든 센서의 위치를 입력받아 오름차순 정렬
sensors = list(map(int, input().split(' ')))
sensors.sort()

# 각 센서 간의 거리를 계산해 내림차순 정렬
distance = []
for i in range(len(sensors) - 1):
    distance.append(sensors[i+1] - sensors[i])
distance.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k - 1):
    distance[i] = 0
print(sum(distance))