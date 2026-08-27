class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #So they need to have the same length
        if len(s) != len(t):
            return False
        #I think I will use a dictionary for this and compare them to each other
        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
        return s_dict == t_dict
