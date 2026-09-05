class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Need to remove spaces
        #Need to make a new string
        #Need to make all character the same letter case

        #Then use two pointer to check both ends and return false if duplicate is found

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