class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # pairing value:frequency in dictionary
        mydict = {}
        for i in nums:
            mydict[i] = mydict.get(i, 0) + 1
        
        #creating a list of lists of size len(nums + 1) such that  all frquencies can listed here
        lst = [ [] for _ in range(len(nums) + 1)]
        for num, freq in mydict.items():
            lst[freq].append(num)

        # traversing from end of lst while checking result is satisfied with k, if yes: return result
        result = []
        for i in range(len(lst) - 1, 0, -1):
            for x in lst[i]:
                result.append(x)
                if len(result) == k:
                    return result
        return []