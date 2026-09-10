class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #So I can replace upto k amount of characters.
        #I need to find the longest repeating characters.
        #If I am starting, I am going to need to keep track of the occurences that the characters appear.
            #With this information I will use it against how many time a character needs to be replaced.
        
        l = 0
        res = 0
        count = {}
        maxC = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            #This gives me the most amount of characters seen for a single character
            maxC = max(maxC, count[s[r]])
            while (r-l+1) - maxC > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res