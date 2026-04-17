class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []
        result = []
         
        pre = 1
        for i in range(len(nums)):
            prefix.append(pre)
            pre *= nums[i]
        
        suf = 1
        for j in range(len(nums) - 1, -1, -1):
            suffix.append(suf)
            suf *= nums[j]

        rev = suffix[::-1]

        for i in range(len(nums)):
            result.append(prefix[i] * rev[i])
        return result