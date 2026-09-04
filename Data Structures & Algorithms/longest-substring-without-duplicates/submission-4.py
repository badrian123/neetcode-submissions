class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #So I am going to iterate through the list of string.
        #Goal is to count substring without duplicates

        #I know i will need res
        res = 0
        l = 0
        seen = set()
        #For r i am going to use the range of the list

        for r in range(len(s)):
            #Ok. now what am i doing exactly?
            #So I am going to need to keep track of the characters seen.
            #ok. What else.
            #Well, I am going to need to check if the character is in seen, else
                #move up.
            
            while s[r] in seen:
                #This is where I would remove and move my left position up
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, (r-l + 1))

        #Seems about right.
        return res