def solution(get_money):
    total_coin_count = 0
    left = 1000 - get_money

    coin_list = [500, 100, 50, 10, 5, 1]
    coin_list.sort(reverse=True)

    for coin in coin_list:
        if left // coin >= 0:
            total_coin_count += left // coin
            left = left % coin

    return total_coin_count

# print(solution((int)(input())))

'''
- 기초적인 탐욕 알고리즘 문제유형
- 큰 화폐단위 부터
'''

changes = 1000 - int(input())
count = 0

for coin in [500, 100, 50, 10, 5, 1]:
    count += changes // coin
    changes %= coin

print(count)