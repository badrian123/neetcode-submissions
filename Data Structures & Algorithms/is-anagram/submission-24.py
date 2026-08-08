class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #So the lengths need to be the same or else you can state that two different size strings are same
        #Can't use two pointers since characters are random positions.
        #So going to use dictionaries to compare to each other.

        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i],0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
        return s_dict == t_dict