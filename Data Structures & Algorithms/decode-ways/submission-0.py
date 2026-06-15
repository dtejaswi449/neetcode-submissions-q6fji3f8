class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}
        def dp(i):

            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0

            memo[i] = dp(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1') or (s[i] == '2' and s[i + 1] < '7'):
                    memo[i] += dp(i + 2)
            
            return memo[i]
        
        return dp(0)
        