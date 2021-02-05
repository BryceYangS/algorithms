'''
https://programmers.co.kr/learn/courses/30/lessons/43163
'''




def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    words.insert(0, begin)
    graph = dict()

    for i in range(len(words) - 1):
        graph[words[i]] = list()
        for j in range(i + 1, len(words)):
            diffCharCnt = 0
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    diffCharCnt += 1
            if diffCharCnt == 1:
                graph[words[i]].append(words[j])

    need_visit = list()
    visited = list()

    need_visit = graph[begin]
    answer = 1
    while need_visit:
        node = need_visit.pop()
        if node == target:
            break
        if node in visited:
            continue
        answer += 1
        visited.append(node)
        need_visit.extend(graph[node])

    return answer


print(solution('hit', 'cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
#
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
#