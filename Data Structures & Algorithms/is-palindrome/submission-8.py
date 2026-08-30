class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Need to make all letters lowercase. - Done
        #isalnum() - Done
        #Will use the two pointer method to examine both sides.
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        l, r = 0, len(new_string)-1

        while l<r:
            if new_string[l] != new_string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True