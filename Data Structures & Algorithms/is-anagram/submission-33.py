class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #So need to check that both strings have the same length
        #Then need to store results in a dictionary
        #Then compare dictionaries to each other.
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        return s_dict == t_dict