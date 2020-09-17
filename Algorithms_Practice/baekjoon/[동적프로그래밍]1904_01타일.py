n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[n])


'''
 - 사용할 수 있는 타일의 종류는 2개
 - 두 가지 종류의 타일 이용, N 길이의 수열을 만드는 모든 경우의 수
 - 가장 전형적인 동적 프로그래밍 문제
 - N이 최대 1,000,000이므로 O(N)으로 해결해야

동적 프로그래밍 문제를 풀기 위해서는 점화석(인접한 항들 사이의 관계식)을 세워야 합니다.
 - eg) D[i] = '수열의 길이가 i일 때의 경우의 수
'''
