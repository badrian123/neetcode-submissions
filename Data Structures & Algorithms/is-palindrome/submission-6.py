class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Id need to lowercase everything.
        #I'd need to ignore the spaces.
        #i'd use a two pointer approach in order to compare and then return false if they aren't the same.

        string = ""

        for c in s:
            if c.isalnum():
                string += c.lower()
        l, r = 0, len(string)-1

        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True