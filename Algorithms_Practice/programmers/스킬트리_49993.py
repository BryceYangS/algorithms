'''
https://programmers.co.kr/learn/courses/30/lessons/49993
'''

def solution(skill, skill_trees):
    answer = 0

    for s in skill_trees:
        tmp_skill = ""
        for char in s:
            if char in skill:
                tmp_skill += char
        if skill[:len(tmp_skill)] == tmp_skill:
            answer += 1
    return answer


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))