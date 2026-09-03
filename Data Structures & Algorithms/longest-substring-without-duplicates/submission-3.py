class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #This one I can use a set.
        #Then the left and right pointer would be sliding window.
            #Left pointer would be 0
            #Right pointer would keep incrementing.
            #Only when we find a duplicate do we move Left pointer to where right pointer is at
            #Every iteration, we are looking for duplicates and increasing count when no duplicates found.
                #Count would get reset the moment a duplicate character is found.
        
        seen = set() #o(1) insertion.
        res = 0
        count = 0
        l = 0
        for r in range(len(s)): #Cuz going to check the entire string.
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res
