'''
https://programmers.co.kr/learn/courses/30/lessons/62049
'''

def solution(n):

    if n == 1:
        return [0]
    else:
        left = solution(n-1).append(0)
        right = solution(n-1)
        right[len(right)//2] = 1
        left.extend(right)
        return left


print(solution(2))