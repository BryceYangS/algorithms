# Stack (스택)
# 데이터를 제한적으로 접근할 수 있는 구조
#   - 한쪽 끝에서만 자료를 넣거나 뺄수 있는 구조
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조 (중요!!)
#  CF) Queue : FIFO
#      Stack : LIFO
#
# 스택 구조
#   스택은 LIFO (Last In, First Out) 또는 FILO (First In, Last Out) 데이터 관리 방식을 따름 ( 스택은 스택 방식이라고 보통 말함 )
#       LIFO : 마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리 정책
#       FILO : 처음에 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책
#   대표적인 스택 활용
#       컴퓨터 내부의 프로세스 구조의 함수 동작 방식
#   주요기능
#       push() : 데이터를 스택에 넣기
#       pop() : 데이터를 스택에서 꺼내기
#
# 스택 구조와 프로세스 스택
#     스택 구조는 프로세스 실행 구조의 가장 기본
#         함수 호출시 프로세스 실행구조를 스택과 비교해서 이해 필요
##          예시) 재귀함수 ---> 함수가 계속해서 호출되고 가장 마지막에 들어간 함수부터 처리됨
def recursive(data):
    if data < 0 :
        print('end')
    else :
        print(data)
        recursive(data - 1)
        print('returned', data)

recursive(4)


# 자료 구조 스택의 장단점
#   장점
#       구조가 단순 --> 구현 쉬움
#       데이터 저장/읽기 속도 빠름
#   단점 (일반적인 스택 구현 시)
#       데이터 최대 개수를 미리 정해야 한다.
#             파이썬의 경우 재귀함수는 1000번까지만 호출 가능
#         저장 공간의 낭비가 발생할 수 있음
#             미리 최대 갯수만큼 저장 공간 확보해야 하기 때문
#   ---> 스택은 단순하고 빠른 성능을 위해 사용되므로, 보통 배열 구조를 활용해서 구현하는 것이 일반적. 이 경우 위와 같은 단점 발생.

data_stack = list()
data_stack.append(1)
data_stack.append(2)
print(data_stack)
print(data_stack.pop())
print(data_stack)

# 프로그래밍 연습 pop, push 기능 구현
print("-----    ------")
stack_list = list()
def push(data):
    stack_list.append(data)

def pop():
    rtn = stack_list[-1]
    del stack_list[-1]
    return rtn

for i in range(10):
    push(i)
print(pop())
