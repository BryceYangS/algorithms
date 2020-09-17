'''
- 가장 긴 증가하는 부분 수열(LIS) 문제는, 전형적인 동적 프로그래밍 문제
- 수열의 크기가 N일 때, 기본적인 동적 프로그래밍 알고리즘으로 O(N^2)에 해결 할 수 있다.


* D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
* 모든 0 <= j < i 에 대해, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]


'''

n = int(input())

a = list(map(int, input().split()))

