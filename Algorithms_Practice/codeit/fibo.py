def fib_optimized(n):

    if n < 3:
        return 1

    previous = 0
    current = 1

    for i in range(2, n + 1):
        now = current + previous
        previous = current
        current = now

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
