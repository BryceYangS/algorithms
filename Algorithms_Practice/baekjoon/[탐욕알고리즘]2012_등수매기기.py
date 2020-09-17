# 5
# 1
# 5
# 3
# 1
# 2

# 3



people_count = int(input())
expected_grade_list = list()
result = 0

for _ in range(people_count):
    expected_grade_list.append(int(input()))

expected_grade_list.sort()

for i in range(people_count):
    result += abs((i + 1) - expected_grade_list[i])

print(result)



'''
 - 예상된 등수와 실제 등수의 차이를 최소화해야 함
 - 이를 위해서, 예상된 등수를 오름차순으로 정렬하면 됨
'''



n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

result = 0
for i in range(1, len(array) + 1):
    result += abs(i - array[i - 1])

print(result)
