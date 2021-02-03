'''
https://programmers.co.kr/learn/courses/30/lessons/42586
'''

def solution(progresses, speeds):
    answer = []

    completeDay = []

    for i in range(len(progresses)):
        tmp = divmod(100 - progresses[i], speeds[i])
        if tmp[1] == 0 :
            completeDay.append(tmp[0])
        else :
            completeDay.append(tmp[0] + 1)

    bf = (0,0)
    for i in range(len(completeDay)):
        if i == 0:
            bf = (0,completeDay[i])
            answer.append(1)
            continue

        if bf[1] >= completeDay[i] :
            answer[bf[0]] += 1
        else :
            bf = (len(answer), completeDay[i])
            answer.append(1)

    return answer



print(solution([93, 30, 55]	, [1, 30, 5]))
#[2, 1]

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
#[1, 3, 2]
