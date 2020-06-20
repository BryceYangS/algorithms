'''
https://www.hackerrank.com/challenges/the-minion-game/problem
'''


def minion_game(string):
    moeum = 'AEIOU'
    stuartScore = 0
    kevinScore = 0

    for i in range(len(string)) :
        tmp = string[i]
        if tmp not in moeum:
            stuartScore += 1
        else:
            kevinScore += 1

        for j in range(i+1, len(string)) :
            tmp += string[j]
            if tmp[0] not in moeum:
                stuartScore += 1
            else:
                kevinScore += 1

    rtnString = ''
    if stuartScore > kevinScore :
        rtnString = 'Stuart ' + str(stuartScore)
    elif stuartScore == kevinScore:
        rtnString = 'Draw'
    else :
        rtnString = 'Kevin ' + str(kevinScore)

    print(rtnString)

s = input()
    # BANANA
minion_game(s)
    # Stuart 12




##############
###SOLUTION###
##############
'''
def minion_game(string):
    # your code goes here

    S_length = len(string)
    player1, player2 = 0, 0

    for i in range(S_length):
        if string[i] in "AEIOU":
            player1 += S_length - i
        else:
            player2 += S_length - i

    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart", player2)
    else:
        print("Draw")
'''