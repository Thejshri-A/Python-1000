def unique_ways(m,n):
    dp = [[1]*n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

# Example usage:
m = 3
n = 7
print(unique_ways(m, n))  # Output: 28