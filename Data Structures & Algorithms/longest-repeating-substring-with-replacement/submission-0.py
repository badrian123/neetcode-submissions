class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxC = 0

        for r in range(len(s)):
            #Were going to be adding characters to dictionary with their number of occurrences.
            count[s[r]] = 1 + count.get(s[r],0)

            #This is keeping track of characters with most occurrences in window
            maxC = max(maxC, count[s[r]])
            #Basically if we know the window size 
                #& maxC is keeping track of repeating characters seen in current window,
                #window size - maxC will give us how many characters that need replacement.
            while (r-l+1) - maxC > k:
                count[s[l]] -= 1
                l += 1
            
            #Now our answer is the window size.
            res = max(res, (r-l+1))

        return res

