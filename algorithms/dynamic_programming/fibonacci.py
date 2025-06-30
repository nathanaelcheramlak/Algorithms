cache = {}
def fib(n):
    if n <= 2:
        return 1
    
    if n - 1 not in cache:
        one = fib(n - 1)
    else:
        one = cache[n - 1]

    if n - 2 not in cache:    
        two = fib(n - 3)
    else:
        two = cache[n - 2]
    
    cache[n] = one + two
    return cache[n]

cache = {1: 1, 2: 1}
def fib(n):
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

seq = [0, 1] * (1000)
def bottom_up(n):
    for i in range(3, n):
        seq[i] = (seq[i - 1] + seq[i - 2])
    
    return seq[n - 1]

for i in range(1, 10):
    print(fib(i), end=' - ')
    print(bottom_up(i))
    # print(seq)