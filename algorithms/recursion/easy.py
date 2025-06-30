def calc(n):
    # print('state', n)
    if n <= 1:
        return 0
    if n % 2 == 1:
        n -= 1
    return n + calc(n - 2)

# print(calc(1)) # adds only even numbers

def fib(n):
    print('state', n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# print(fib(4))
# 0, 1, 1, 2, 3, 5, 8, 13, 21

def mul(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    
    return mul(n - 3) * mul(n - 2) * mul(n - 3)

# print(mul(5))
# 1, 2, 3, 6, 36, 648

def sum_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_digit(n // 10)

# print(sum_digit(698))

def harmonic(n):
    if n <= 1:
        return 1
    return 1 / n + harmonic(n - 1)

# print(harmonic(7))

def gcd(n, m, div=2, ans=1):
    if div > n or div > m:
        return ans
    if n % div == 0 and m % div == 0:
        ans *= div
        n //= div
        m //= div
        return gcd(n, m, div, ans)

    return gcd(n, m, div + 1, ans)

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

print(gcd(14, 24))
# 20 1 2
# 12 1 2