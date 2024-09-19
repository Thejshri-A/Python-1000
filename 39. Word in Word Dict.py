def word_in_word_dict(s, word_dict):
    dp = [False]*(len(s)+1)
    dp[0]= True #Accounts for an empty string
    
    for i in range(1, len(s)+1):
        for word in word_dict:
            if dp[i-len(word)] and s[i-len(word): i ]==word:
                dp[i]=True
    return dp[-1]

# Example
s = "leetcode"
word_dict = ["leet", "code"]
print(word_in_word_dict(s, word_dict))  # Output: True