class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        if len(s) <= 1:
            return len(s)
        start = 0
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[end])
            res = max(res, (end - start + 1))
        return res