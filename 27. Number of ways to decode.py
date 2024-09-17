def num_of_decodings(s):
    if not s:
        return 0
    dp = [0]*(len(s)+1)
    dp[0], dp[1] = 1, 1 if s[0]!= '0' else 0
    
    for i in range(2, len(s)+1):
        if s[i-1] != '0':
            dp[i] +=dp[i-1]
        if '10'<= s[i-2:i]<= '26':
            dp[i] +=dp[i-2]
    return dp[-1]


s='226'
print(num_of_decodings(s))