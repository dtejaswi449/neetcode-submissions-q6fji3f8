class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def ap(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(ap(i + 1), nums[i] + ap(i + 2))
            return memo[i] 
        
        nemo = {}
        def bp(i):
            if i >= len(nums):
                return 0
            if i in nemo:
                return nemo[i]
            nemo[i] = max(bp(i + 1), nums[i] + bp(i + 2))
            return nemo[i]

        
        return max(ap(0), bp(1)) if len(nums) > 1 else nums[0]