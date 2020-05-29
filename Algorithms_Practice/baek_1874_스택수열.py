# Stack
# 핵심아이디어
#   1.스택에 원소를 삽입할 때는, 단순히 특정 수에 도달할때까지 삽입하면 됨
#   2.스택에서 원소를 연달아 빼낼 때 내림차순을 유지할 수 있는지 확인

# def solution() :
#     # 입력값 입력받음
#     n = int(input())
#     compare = list()
#     for i in range(0,n):
#         compare.append(int(input()))
#
#     data = list(range(1,n+1))
#     stack_list = list()
#     output = list()
#
#     # 사용자가 출력하려는 수열 반복문 돌리기
#     for val in compare:
#         if val in data:
#             for i in range(0, data.index(val)+1):
#               stack_list.append(data[i])
# #               output.append("+")
# #             del data[0:data.index(val)+1]
# #             stack_list.pop()
# #             output.append("-")
# #         else:
# #             if stack_list[-1] == val:
# #                 stack_list.pop()
# #                 output.append("-")
#             else:
#                 output.append("NO")
#                 break
#     if output[-1] != "NO":
#         for print_word in output:
#             print(print_word)
#     else :
#         print(output[-1])
#
# solution()
## ----> 백준 Python 3 : 시간초과 / PyPy 3 : 정답

n = int(input())

count = 1
stack = []
result = []

for i in range(1, n + 1): # 데이터 개수만큼 반복
    data = int(input())
    while count <= data: # 입력받은 데이터에 도달할때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else: # 불가능한 경우
        print('NO')
        exit(0)

print('\n'.join(result)) # 가능한 경우