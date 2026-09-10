class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #So going to have to find the longest substring without duplicates.
        
        #Going to start at the very begining.
        #Going to need a set.
        #Going to check if character is in set.
            #This should determine if we move the left pointer.
        
        seen = set()
        res = 0
        l = 0
        for r in range(len(s)):
            #Going to remove all of the characters in set until l is at r
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r-l+1)
        return res