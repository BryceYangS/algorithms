# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# input==================
# 5
# 5
# 2
# 3
# 4
# 1
# output==================
# 1
# 2
# 3
# 4
# 5


# 선택정렬 ( O(n^2) )
# 제일 작은 값 또는 제일 큰 값을 맨 앞에서부터 차례차례 보냄
def selection_sort(arr):
    for i in range(len(arr) - 1):
        lowest_idx = i # 가장 작은 원소의 인덱스
        for j in range(i+1, len(arr)):
            if arr[lowest_idx] > arr[j]:
                lowest_idx = j
        arr[i], arr[lowest_idx] = arr[lowest_idx], arr[i]
    return arr

# 기본 정렬 라이브러리 ( O(NlogN)
def basic_sort_lib(arr):
    arr.sort()
    return arr

number_count = (int)(input())
number_arr = []
for _ in range(number_count):
    number_arr.append((int)(input()))

print(basic_sort_lib(number_arr))