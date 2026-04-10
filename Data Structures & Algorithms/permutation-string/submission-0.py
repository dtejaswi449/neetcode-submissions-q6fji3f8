class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        d1 = {}
        for i in s1:
            d1[i] = 1 + d1.get(i, 0)
        d2 = {}
        # for i in s2:
        #     d2[s2[i]] = 1 + d2.get(s2[i], 0)
        start = 0
        for end in range(len(s2)):
            d2[s2[end]] = 1 + d2.get(s2[end], 0)
            if len(s1) == (end - start + 1):
                if d1 == d2:
                    return True
                else:
                    d2[s2[start]] -= 1
                    if d2[s2[start]] == 0:
                        del d2[s2[start]]
                    start += 1
        return False