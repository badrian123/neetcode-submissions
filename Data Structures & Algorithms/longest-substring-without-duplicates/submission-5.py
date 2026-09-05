class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #So I am going to iterate through the string.
        #I am going to need to keep track of results.
        #I am going to keep track of what characters i have seen.
            #Set()
        
        #As I am iterating, I am using two pointers.
        #The left pointer is keeping track of the start of the substring.
        #The right pointer is moving throughout the substring, scanning.
        #The moment I find a duplicate, that is when I am going to have to move the left pointer.
            #It's going to

        seen = set()
        res = 0
        l, r = 0, 0
        while r < len(s):
            #Going to be scanning.
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            res = max(res, r-l+1)
            r += 1
        return res