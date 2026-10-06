# Word Break:
def word_break(s,wordDict):
    dp = [True] + [False] * len(s)
    for indx in range(1,len(s)+1):
        for word in wordDict:
            if dp[indx - len(word)] and s[:indx].endswith(word):
                dp[indx] = True
    return dp[-1] 
s = "leetcode"
wordDict = ["leet", "code"]
res = word_break(s,wordDict)
print(res) 
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]  
res1 = word_break(s,wordDict)
print(res1)     