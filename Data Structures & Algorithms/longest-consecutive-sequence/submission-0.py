class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        s = set(nums)
        count = 0
        for i in s:
            if i - 1 not in s:
                num = i
                temp = 1
                while num + 1 in s:
                    temp += 1
                    num += 1
                count = max(temp, count)
        return count
