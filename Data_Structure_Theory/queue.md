## Queue로 만들기 . 일반적인 큐는 FIFO (First-In, First-Out)

```python
import queue


fifo_queue = queue.Queue()
fifo_queue.put("funcoding")
fifo_queue.put(1)
print(f'Queue Size : {fifo_queue.qsize()} / First Data Out : {fifo_queue.get()}')


## LifoQueue LIFO(Last-In, First-Out)
data_queue = queue.LifoQueue()
data_queue.put("funcoding")
data_queue.put(1)
print(f'Queue Size : {data_queue.qsize()} / First Data Out : {data_queue.get()}')
```

## PriorityQueue()로 큐 만들기
 - 각각의 데이터마다 우선순위를 집어넣음. 우선순위에 따라 데이터를 추출.
 - 우선순위 값이 낮을수록 먼저 나옴
 
 ```python
prior_queue = queue.PriorityQueue()
prior_queue.put((10,"korea")) # 우선순위, 값 을 튜플로 넣어줌
prior_queue.put((5,1))
prior_queue.put((15,"china"))
print(f'1: {prior_queue.get()} 2: {prior_queue.get()}')
```

## 큐 어디에 많이 쓰일까??
 - 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨
 - 큐의 경우에는 장단점 보다는 (특별히 언급되는 장단점 없음), 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음

## Practice!
```python
queue_list = list()
def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for i in range(10):
    enqueue(i)

print(f'len : {len(queue_list)} / out : {dequeue()} , out2 : {dequeue()}')
```
