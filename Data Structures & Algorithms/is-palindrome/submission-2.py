class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for v in s:
            if v.isalnum():
                new_string += v.lower()
        
        l, r = 0, len(new_string)-1
        while l < r:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1
        return True