def solution(A, B):
    A.sort()
    # B.sort()
    B = sorted(set(B))
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i] or (i < len(B) - 1 and a == B[i+1]):
            return a
    return -1


print(solution([2, 1], [3, 3]))
print(solution([2, 3, 4, 5], [1, 5, 6, 7, 1, 1, 1, 2])) # 2
print(solution([2, 3, 4, 5, 6, 7], [11, 12, 7])) # 7
print(solution([2, 3, 4, 5, 6, 7], [11, 12, 13, 7, 9, 8, 7])) # 7
print(solution([7,7,1,2,3,2,4,5], [11, 12, 13, 7, 9, 8, 7])) # 7
print(solution([2,2,2,4,7], [11, 13,15,12, 13, 7, 9, 8, 7])) # 7
print(solution([2,2,2,4,7], [11, 13,15,12, 13, 7, 9, 8, 7])) # 7
print(solution([2,2,1,1,1,1,1,3,4,5,6,7,8,9,34,2,2,4,7], [11, 13,15,12, 13, 7, 9, 8, 7,3])) # 3
print(solution([2,3,4,5,6,7,8,9,10], [10,2,2,2,2,2,2,2,3,12])) # 2
print(solution([2,4,6,10,10], [3,5,7,8,10,12])) # 10
print(solution([2,4,6,10,12], [3,5,7,8,10,12])) # 10
print(solution([2,4,6,8,10], [1,3,5,7,9,10])) # 10
print(solution([2,4,6,10,12], [1,3,5,7,9,11,12])) # 10


