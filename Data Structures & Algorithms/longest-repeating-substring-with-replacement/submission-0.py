class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = {}
        res = 0
        maxchar = 0
        start = 0
        for end in range(len(s)):
            tracker[s[end]] = 1 + tracker.get(s[end], 0)
            maxchar = max(maxchar, tracker[s[end]])
            
            if (end - start + 1) - maxchar > k:
                 tracker[s[start]] -= 1
                 start += 1
           
            res = max(res, end - start + 1)
        return res