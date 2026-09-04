class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Going to use dictionaries to keep track of what has been seen.
        #String length will need to be same in order to proceed forward.
        #Basically going to be iterating the string and storing it's character into dicitonary.
        #Then comparing dictionaries to each other in order to see if they match.
        #If they do then they are anagrams. Else, they aren't.

        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        return s_dict == t_dict