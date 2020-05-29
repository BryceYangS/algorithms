'''
https://www.acmicpc.net/problem/5397
'''

'''
count = (int)(input())
user_input_list = list()

for _ in range(count):
    user_input_list.append(list(map(str,input())))


for i in range(len(user_input_list)):
    user_input = user_input_list[i]
    output = list()
    cursor = 0

    for index in range(len(user_input)):
        char = user_input[index]
        if char == '<':
            if cursor == 0 :
                cursor = 0
            else :
                cursor -= 1
        elif char == '>':
            if cursor == 0 :
                cursor = 0
            elif cursor == len(output):
                pass
            else :
                cursor += 1
        elif char == '-':
            if len(output) > 0:
                output.pop(cursor-1)
        else :
            output.insert(cursor,char)
            cursor += 1
    print(''.join(output))

--> Runtime Error 뜸...
'''


'''
문제풀이 핵심 아이디어 

    1. 문자열 크기가 최대 1,000,000이므로 시뮬레이션 방식으로는 문제를 해결할 수 없습니다.
    2. 스택을 활용해 선형시간 문제를 해결할 수 있는 알고리즘을 설계합니다.

설게 구조
  ----------------------------------
    left_stack | 커서 | right_stack
  ----------------------------------

'''



test_case = (int)(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else :
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
