def wordBreak(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[0] = True
    
    for i in range(1, len(s)+1):
        for word in wordDict:
            if dp[i-len(word)] and s[i-len(word): i] == word:
                dp[i]=True
    return dp[-1]

# Example usage:
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # Output: True