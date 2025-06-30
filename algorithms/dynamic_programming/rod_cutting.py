prices = [1, 5, 8, 9, 10, 17, 17, 20]

# Bottom Up Approach
cache = {}
def rod_cutting(n):
    if n == 1:
        return prices[0]
    
    for l in range(1, n + 1):
        temp = prices[l - 1]
        for pos_cut in range(1, l // 2 + 1):
            temp = max(temp, prices[pos_cut - 1] + prices[l - pos_cut- 1])
        cache[l] = temp
    
    return cache[n]




# print(rod_cutting(8))

prices = [1, 5, 8, 9, 10, 17, 17, 20]

def rod_cutting(n):
    dp = [0] * (n + 1)  # dp[i] = max revenue for rod of length i

    for length in range(1, n + 1):
        max_val = 0
        for cut in range(1, length + 1):
            max_val = max(max_val, prices[cut - 1] + dp[length - cut])
        dp[length] = max_val

    return dp[n]

# print(rod_cutting(8))  # Output: 22


def rod_cutting(length):
    if length <= 0:
        return 0
    curr_max = prices[length]
    for cut in range(length + 1):
        curr_max = max(curr_max, rod_cutting(cut) + rod_cutting(length - cut))
    return curr_max

prices = [0, 1]
print(rod_cutting(len(prices) - 1))