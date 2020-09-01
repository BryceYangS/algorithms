def mySolution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n > 3:
        return mySolution(n-1) + mySolution(n-2) + mySolution(n-3)

print(mySolution(5))