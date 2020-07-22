# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    bin_ab = bin(A*B)[2:]
    answer = 0
    for char in bin_ab:
        if char == '1':
            answer += 1

    return answer


print(solution(3, 7))