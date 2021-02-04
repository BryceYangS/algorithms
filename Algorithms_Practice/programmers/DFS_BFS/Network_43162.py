'''
https://programmers.co.kr/learn/courses/30/lessons/43162?language=python
'''

def solution(n, computers):
    answer = 0


    graph = dict()

    for i in range(len(computers)):
        graph[str(i)] = list()
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[str(i)].append(str(j))

    while len(graph.keys()) > 0:
        need_visit = list()
        visited = list()
        need_visit.append(list(graph.keys())[0])
        while need_visit:
            node = need_visit.pop()

            if node not in visited:
                need_visit.extend(graph[node])
                visited.append(node)
        for key in visited:
            del graph[key]
        answer += 1

    return answer



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))
# 1d
