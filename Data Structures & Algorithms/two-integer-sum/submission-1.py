class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in mydict:
                return [mydict[val], i]
            mydict[nums[i]] = i
        return []

# TC: O(N)
# SC: O(N)