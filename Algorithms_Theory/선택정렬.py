'''
1. 선택정렬(Selection Sort) 이란?
 - 다음과 같은 순서를 반복하며 정렬하는 알고리즘
    1. 주어진 데이터 중 최소값을 찾음
    2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
    3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복

====> 최소값을 선택한다! 라고 암기하자

    https://visualgo.net/en/sorting
'''

'''
for i in range(데이터길이 -1):
    lowest_idx = i
    for j in range(i+1, 데이터길이):
        if 데이터[lowest_idx] > 데이터[j]:
            lowest_idx = j
    데이터[i], 데이터[lowest_idx] = 데이터[lowest_idx], 데이터[i]
'''

def selection_sort(data):

    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    return data

import random
data_list = random.sample(range(100),10)
print(selection_sort(data_list))