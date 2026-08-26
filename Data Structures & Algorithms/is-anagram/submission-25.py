class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Needs to be of same length
        if len(s) != len(t):
            return False
        
        #Going to use dictionary in order to compare and return if anagrams are same or different
        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
        return s_dict == t_dict

