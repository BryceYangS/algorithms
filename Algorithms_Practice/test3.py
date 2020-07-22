# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations


def solution(S):
    # write your code in Python 3.6
    cnt_a = 0
    for char in S:
        if char == 'a':
            cnt_a += 1

    if cnt_a % 3 != 0:
        return 0
    elif cnt_a == 0:
        items = [i for i in range(len(S) - 1)]
        # len(combinations(len))
        return len(list(combinations(items, 2)))
    else:
        tmp_num = divmod(cnt_a, 3)
        a_cnt = 0
        tmp_arr = []
        tmp_tuple = ()
        for i in range(len(S)):
            if S[i] == 'a':
                a_cnt += 1
                if tmp_num[0] == 1:
                    tmp_arr.append(i)
                else:
                    if len(tmp_tuple) == 0:
                        tmp_tuple = (i,)
                    if a_cnt == tmp_num[0]:
                        tmp_tuple += (i,)
                        tmp_arr.append(tmp_tuple)
                        tmp_tuple = ()
                        a_cnt = 0
        if tmp_num[0] ==1:
            return (tmp_arr[1] - tmp_arr[0]) * (tmp_arr[2] - tmp_arr[1])
        else:
            return (tmp_arr[1][0] - tmp_arr[0][1]) * (tmp_arr[2][0] - tmp_arr[1][1])





print(solution('babaa')) # 2 : ba | ba | a   /// bab | a | a
print(solution('ababa')) # 4 : a | ba | ba   ///  ab | a | ba /// a | bab | a  /// ab | ab | a
print(solution('ababbaabaa'))