def sol1(A, M):
    q = A
    for _ in range(M):
        a = q.pop(0)
        q.append(a)

    return q.pop(0)


def sol2(N, M, Ci):
    cheese = []
    for i in range(len(Ci)):
        cheese.append([Ci[i], i])

    pan = cheese[0:N]
    cheese = cheese[N:]
    completed = []

    while pan:
        for j in range(len(pan)):
            pan[j][0] //= 2
            if pan[j][0] == 0:
                completed.append(pan[j])
                if cheese:
                    pan[j] = cheese.pop(0)
                else:
                    pan[j] = [-1, -1]
        if len(completed) == M:
            break
    return completed[-1][1] + 1


def sol3(N, M):
    graph = dict()
    start = tuple()
    end = tuple()

    for i in range(len(N)):
        for j in range(len(N)):
            if M[i][j] == 2:
                start = (i, j)
            elif M[i][j] == 3:
                end = (i, j)

    graph[start] = list()

    for row in [-1, 0, +1]:
        for col in [-1, 0, +1]:
            r = start[0] + row
            c = start[1] + col
            if r > -1 and c > -1 and M[r][c] == 0:
                graph[start].append()

# print(sol1([5527, 731, 31274], 10))
# print(sol1([1,2,3,4,5], 12))
# print(sol1([1,2,3,4,5,6,7,8,9,10], 23))

# print(sol2(3, 5, [7, 2, 6, 5, 3]))
# print(sol2(5, 10, [5,9,3,9,9,2,5,8,7,1]))
# print(sol2(5, 10, [20,4,5,7,3,15,2,1,2,2]))

print(sol3(5, [[1, 3, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 2, 1]]))
