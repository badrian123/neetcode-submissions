class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Palindrome
            #Ignores all non-alphanumeric characters
                #So no spaces.
        
        #Output, return True if string is a palindrome else False.
        
        #Approach.
            #Going to work on this first.
            #Will need to prepare the string in order for iteration to work.
                #Going to create a new string that has spaces removed. isalnum() -Done
                #Keeps all characters that same -Done
                    #So no mix of capital letters with lowercase letters, just all letters the same.
            
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c.lower()

            #Going to work on the second.
            #Two pointer method.
                #Examine both sides to each other until characters from both side don't match or run out of characters.
        l,r = 0, len(new_string)-1
        while l < r:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1
        return True