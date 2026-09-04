class Solution:
    def isPalindrome(self, s: str) -> bool:
        #ignores all non alphanumeric characters.
        #reads the same forward and backward.

        #Output:
            #Return true if palindrome else false

        #So no spaces.
        # I am going to start off by getting rid of all non alphanumeric characters.
        #Create a new string.
            #Store all alphanumeric characters in the string.
            #lowercase.
        #Check use two pointers at each end of the string to compare the characters against each other.
            #If they false.
            #else return true once we have checked all of the characters in the string.
        
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