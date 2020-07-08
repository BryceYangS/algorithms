'''
https://programmers.co.kr/learn/courses/30/lessons/43165
'''

def solution(numbers, target):
    answer = 0

    def dfs(numbers, target, sum, idx):
        if idx == len(numbers):
            if sum == target :
                nonlocal answer
                answer += 1
            return
        dfs(numbers, target, sum + numbers[idx], idx+1)
        dfs(numbers, target, sum - numbers[idx], idx+1)

    dfs(numbers, target, 0, 0)

    return answer



print(solution([1, 1, 1, 1, 1], 3)) # 5