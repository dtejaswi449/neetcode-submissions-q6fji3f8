class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        myset = set(wordDict)
        memo = {}

        def dp(i):

            if i in memo:
                return memo[i]
            
            if i == len(s):
                return True
            
            memo[i] = False
            for end in range(i + 1, len(s) + 1):
                word = s[i: end]
                if word in myset and dp(end):
                    memo[i] = True
                    
            
            return memo[i]
        
        return dp(0)