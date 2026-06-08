class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')
            
            if rem in memo:
                return memo[rem]

            # best = float('inf')
            # for c in coins:
            #     result = dp(rem - c) + 1
            #     if result < best:
            #         best = result

            memo[rem] = min(1 + dp(rem - c) for c in coins)
            return memo[rem]

        ans = dp(amount)
        return ans if ans != float('inf') else -1