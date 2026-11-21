def coinChange(coins, amount):
    big = amount + 1
    dp = [big] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i >= c and dp[i - c] != big:
                dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[amount] == big:
        return -1
    return dp[amount]


if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))   # 3
    print(coinChange([2], 3))          # -1
    print(coinChange([1], 0))          # 0
    print(coinChange([2, 5], 11))      # 4