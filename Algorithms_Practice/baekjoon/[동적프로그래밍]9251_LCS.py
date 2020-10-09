'''
ACAYKP
CAPCAK

30분

두 수열이 주어졌을 때, 두 수열 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾아야 합니다.
가장 긴 공통 부분 수열(LCS) 문제로 알려진 대표적인 동적 프로그래밍 문제
두 수열 길이가 N 미만일 때, 시간복잡도 O(N^2)으로 문제 해결 가능


두 수열을 각각 X, Y
D[i][j] = X[0 ... i]와 Y[0 ... j]의 공통 부분 수열의 최대 길이
두 문자열의 길이를 조금씩 늘려 가며 확인하여, 공통 부분 수열의 최대 길이를 계산합니다.


D[i][j] =    D[i - 1][j - 1] + 1     if X[i]= Y[j]
             max(D[i][j - 1], D[i - 1][j])

'''

x = input()
y = input()


arr = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])


print(arr[len(x)][len(y)])