'''
https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
'''
import math

def solution(lines):
    answer = 0

    first_log = lines[0].split(' ')
    start_times = first_log[1].split(':')
    start_times = (int)(start_times[0])*3600 + (int)(start_times[1])*60 + (float)(start_times[2])
    start_times = math.ceil(((float)(format(start_times+0.001,'.3f')) - (float)(first_log[2][:-1])))

    last_log = lines[-1].split(' ')
    end_times = last_log[1].split(':')
    end_times = (int)(end_times[0])*3600 + (int)(end_times[1])*60 + math.trunc((float)(end_times[2]))
    if start_times == end_times:
        return 1
    for i in range(start_times, end_times+1):
        count = 0
        for log in lines:
            tr_end_time = log.split(' ')[1].split(':')
            tr_end_time = (int)(tr_end_time[0]) * 3600 + (int)(tr_end_time[1]) * 60 + (float)(tr_end_time[2])
            tr_st_time = convertToTrStTimeSnds(tr_end_time, log.split(' ')[2][:-1])
            if (tr_st_time >= i and tr_st_time < i+1) or (tr_st_time < i and tr_end_time < i+1):
                count += 1

        if answer < count:
            answer = count
    print(answer)
    return answer

def convertToTrStTimeSnds(end_time, pro_time):
    tr_st_time = end_time + 0.001 - (float)(pro_time)
    return tr_st_time

# solution([
# '2016-09-15 01:00:04.001 2.0s',
# '2016-09-15 01:00:07.000 2s'])


# solution(["2016-09-15 00:00:00.000 3s"])
# solution(["2016-09-15 23:59:59.999 0.001s"])
# solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
# solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
# solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"])