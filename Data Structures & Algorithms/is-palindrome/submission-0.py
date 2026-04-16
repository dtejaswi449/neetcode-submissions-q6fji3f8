class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = []
        for i in s:
            if (ord(i) >= ord("a") and ord(i) <= ord("z")) or (ord(i) >= ord("0") and ord(i) <= ord("9")):
                lst.append(i)
        return lst[::-1] == lst