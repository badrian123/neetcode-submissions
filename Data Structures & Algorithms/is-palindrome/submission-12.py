class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Going to have to remove non-alphanumeric characters.
        #Going to have to make all the character same letter case
        #Going to use two pointer in order to solve the problem.

        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        
        l, r = 0, len(new_string)-1
        while l < r:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1
        return True