# Linked List
#
# 링크드 리스트 구조
#     연결 리스트라고도 함
#     배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
#     링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
#     본래 C언어에서는 주요한 데이터 구조지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원
#
#     링크드 리스트 기본 구조와 용어
#         Node : 데이터 저장 단위(데이터값, 포인터)로 구성
#             -- 링크드 리스트는 데이터 + 다음 데이터 주소값(포인터)을 가리키는 주소를 같이 저장
#         Pointer : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
#
# Node 구현
#     보통 파이썬서 링크드 리스트 구현시, 파이썬 클래스 활용
#     참고 : https://www.fun-coding.org/PL&OOP1-3.html

# class Node1:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Node:
#     def __init__(self, data, next=None):
#         # 인자가 1개만 넘어올 경우 next 값을 None으로 설정
#         self.data = data
#         self.next = next
#
# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# head = node1

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
for i in range(2,10):
    add(i)

print_node = head
while print_node.next:
    print(print_node.data)
    print_node = print_node.next
print(print_node.data)

# 링크드 리스트의 장단점 (전통적인 C언어에서의 배열과 링크드 리스트)