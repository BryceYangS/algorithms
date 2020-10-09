'''
40분

3 5 10
5 3 7

- 차례대로 곡을 연주한다는 점에서, 동적 프로그래밍으로 해결할 수 있는 문제
- 곡의 개수가 N, 볼륨의 최댓값은 M
- 동적 프로그래밍을 이용해 시간복잡도 O(NM)으로 해결 가능

*핵심 아이디어*
 - 모든 볼륨에 대해 연주 가능 여부 계산
 - D[i][j+1] = i번째 노래일 때 j 크기의 볼륨으로 연주 가능한지 여부
 - 노래를 순서대로 확인하며, 매 번 모든 크기의 볼륨에 대해 검사

 - D[i][j - V[i]] = True if D[i - 1][j] = True
 - D[i][j + V[i]] = True if D[i - 1][j] = True
'''

n, s, m = map(int, input().split(' '))
v = list(map(int, input().split(' ')))

arr = [[0] * (m+1) for _ in range(n+1)]

print(arr)