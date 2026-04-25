class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) == 0:
            return ""
        
        reslen = float("inf")
        res = ""
        countT = {}
        window = {}
        
        
        for i in t:
            countT[i] = countT.get(i, 0) + 1
            window[i] = 0

        have, need = 0, len(countT)
        

        start = 0
        for end in range(len(s)):
            if s[end] in window:
                window[s[end]] = 1 + window.get(s[end], 0)
                if window[s[end]] == countT[s[end]]:
                    have += 1
            while have == need:
                if (end - start + 1) < reslen:
                    reslen = end - start + 1
                    res = s[start:end + 1]
                
                if s[start] in window:
                    window[s[start]] -= 1
                    if window[s[start]] < countT[s[start]]:
                        have -= 1
                start += 1
        
        return res