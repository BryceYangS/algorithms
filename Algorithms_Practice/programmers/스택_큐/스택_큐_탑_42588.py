'''
https://programmers.co.kr/learn/courses/30/lessons/42588
'''


def solution(heights):
    answer = []
    # answer = [0] * len(heights)  --> 이런식으로 미리 선언해놓으면 18번째 라인 필요 없음
    
    for i in range(len(heights) - 1, 0, -1):
        receive_tower = 0
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                receive_tower = j + 1
                break
        answer.append(receive_tower)

    answer.append(0)

    return list(reversed(answer))


print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))