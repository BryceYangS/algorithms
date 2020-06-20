'''
https://programmers.co.kr/learn/courses/30/lessons/42839
'''
from itertools import permutations


def solution(numbers):
    answer = 0
    num = list(numbers)

    numArr = []

    for i in range(1,len(num)+1):
        permutaionNumbers = list(set(list(permutations(num, i))))
        for t in permutaionNumbers:
            if t[0] == '0':
                continue
            tmpNum = int(''.join(t))
            if isPrime(tmpNum):
                answer += 1
    return answer

def isPrime(number):
    # 1이 아니면
    if number != 1:
        for f in range(2, number):
            # 나눠지는 수가 있으면 소수 아님
            if number % f == 0:
                return False
    # 1일 경우 소수 아님
    else:
        return False

    return True


# print(solution('17')) # 3
print(solution('011')) # 2
