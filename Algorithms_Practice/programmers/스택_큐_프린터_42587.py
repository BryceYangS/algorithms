'''
https://programmers.co.kr/learn/courses/30/lessons/42587
'''
def solution(prior, loc):
    answer = 0
    queue = [(i, idx) for idx, i in enumerate(prior)]
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == loc:
                answer = count
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


    return answer


print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5