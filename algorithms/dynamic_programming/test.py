def cutRod(price):
    n = len(price)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        current = price[i - 1]
        for cut in range(i + 1):
            current = max(current, dp[cut] + dp[i - cut])
        dp[i] = current
    print('DP: ', list(enumerate(dp)))
    
    return dp[-1]

# print(cutRod([1, 5, 8, 9, 10, 17, 17, 20]))


def rod_cutting(length):
    if length <= 0:
        return 0
    curr_max = prices[length - 1]
    for cut in range(1, length):
        curr_max = max(curr_max, rod_cutting(cut) + rod_cutting(length - cut))
    return curr_max

prices = [1, 5, 8, 9, 10, 17, 17, 20]
print(rod_cutting(len(prices)))