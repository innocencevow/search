def numSquares(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]


if __name__ == "__main__":
    print(numSquares(12))   # 3，12 = 4 + 4 + 4
    print(numSquares(13))   # 2，13 = 4 + 9
    print(numSquares(1))    # 1
    print(numSquares(0))    # 0