data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1으로 바꾸는 경우

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1


print(min(count0, count1))


'''
- 문자열에 있는 숫자를 모두 0 혹은 1로 만들어야 한다
  --> 모두 0인 경우 / 모두 1인 경우 두 가지 경우 모두 계산
'''