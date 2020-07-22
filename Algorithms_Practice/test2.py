from itertools import combinations
def solution(A, F, M):
    # write your code in Python 3.6

    def isOverDiceNum(nums_arr, missing_num_total):
        for i in range(len(nums_arr)):
            if nums_arr[i] + 1 > 6:
                return True
        if (missing_num_total - (nums_arr[-1] + 1)) > 6:
            return True
        return False


    # 총 주사위 굴린 횟수
    cnt = len(A) + F

    missing_num_total = (cnt * M) - sum(A)

    if missing_num_total <= 0:
        return [0]
    elif missing_num_total > 6*F:
        return [0]

    items = [ i for i in range(missing_num_total-1) ]
    nums = list(combinations(items,F-1))

    answer = []
    for i in range(len(nums)):
        if isOverDiceNum(nums[i], missing_num_total):
            continue
        # tmp_F_arr = []
        for j in range(len(nums[i])):
            if j == 0:
                answer.append(nums[i][j]+1)
            else:
                answer.append(nums[i][j] - nums[i][j-1])
        answer.append(missing_num_total - (nums[i][-1] + 1))
        # answer.append(tmp_F_arr)
        break



    return answer



# A : 주사위 결과
# F : 정수
# M : 산술평균


# print(solution([6, 1], 1, 1)) #[0]
# print(solution([3,2,4,3],2,4)) #[6,6]
print(solution([1,5,6],4,3)) #[2,1,2,4] /