def coinChange(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0]=0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
        
    return dp[i] if dp[i]!=float('inf') else -1

coins = [2, 5, 10]
amount = 12

print(coinChange(coins, amount))