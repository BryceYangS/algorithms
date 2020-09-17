'''
- 배낭 문제(Knapsack Problem)으로도 알려져 있는, 전형적인 동적 프로그래밍 문제
- 물품의 수가 N, 배낭에 담을 수 있는 무게가 K
- 동적 프로그래밍을 이용해 시간 복잡도 O(NK)로 문제 해결 할 수 있습니다.



핵심 아이디어 : 모든 무게에 대하여 최대 가치를 저장하기
D[i][j] = 배낭에 넣은 물품의 무게 합이 j 일 때 얻을 수 있는 최대 가치
각 물품의 번호 i에 따라서 최대 가치 테이블 D[i][j]를 갱신하여 문제를 해결 할 수 있다.

각각의 물품에 대해서 K번 계산 필요 ---> O(NK)

'''


'''
4 7
6 13
4 8
3 6
5 12
'''

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    weight, value = map(int, input().split())
    for j in range(1, k + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])


# print(dp)