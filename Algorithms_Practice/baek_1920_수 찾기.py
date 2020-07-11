'''
https://www.acmicpc.net/problem/1920
'''
def solution(n, a, m, b):
    for findNum in b:
        if findNum in a:
            print(1)
        else :
            print(0)

user_input1 = (int)(input())
user_input2 = set(map(int, input().split()))
user_input3 = (int)(input())
user_input4 = list(map(int, input().split()))

solution(user_input1,user_input2,user_input3, user_input4)

### Input ###
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

### Output ###
# 1
# 1
# 0
# 0
# 1