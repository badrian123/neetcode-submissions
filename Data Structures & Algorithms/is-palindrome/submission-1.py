class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        L, R = 0, len(new_s)-1
        while L < R:
            if new_s[L] != new_s[R]:
                return False
            L += 1
            R -= 1
        return True