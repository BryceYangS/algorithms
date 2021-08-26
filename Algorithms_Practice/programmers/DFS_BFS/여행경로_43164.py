'''
https://programmers.co.kr/learn/courses/30/lessons/43164
'''


def solution(tickets):
    answer = []

    table = dict()

    for (start, end) in tickets:
        if start not in table.keys():
            table[start] = []
        table[start].append(end)

    for key in table.keys():
        table[key].sort()

    answer = dfs(table, len(tickets))

    return answer


def dfs(graph, airConut):
    visited = []
    need_visit = ['ICN']

    while need_visit:
        node = need_visit.pop(0)
        visited.append(node)
        if node not in graph.keys() or len(graph[node]) <= 0:
            if len(visited) == airConut + 1:
                return visited
        next_visit = graph[node].pop(0)
        need_visit.append(next_visit)


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
# [ICN, JFK, HND, IAD]

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))
# [ICN, ATL, ICN, SFO, ATL, SFO]
