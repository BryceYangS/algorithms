
num = input()

num = [int(i) for i in num]

count = [0, 0]

for i in range(2):
    if i != num[0]:
        count[i] += 1
    for j in range(1,len(num)):
        if i == num[j]:
            continue
        if i != num[j] and num[j - 1] != num[j]:
            count[i] += 1

print(min(count))


'''
입력숫자 = [0,0,0,1,1,0,0]
숫자2개 = [0,1]
숫자2개 통일하기 위해 각각 뒤집는 횟수(count) = [0,0]

for i in range(len(숫자2개)): # 1인 경우/ 2인 경우 처리 위해 Loop
    if 입력숫자[0] != 숫자2개[i]: # 처음 숫자가 통일하려는 숫자랑 다를 경우 뒤집음
         count[i] += 1
     
    for j in range(1, len(입력숫자)): # 나머지 입력숫자 뒤집기 시행
        if 입력숫자[j] == 숫자2개[i]: # 통일하려는 숫자와 입력받은 숫자 동일 경우 뒤집지 않음
            continue
        if 입력숫자[j - 1] != 입력숫자[j] : # 앞의 숫자에서 뒤집지 않은 경우 뒤집어줌
            count[i] += i
'''