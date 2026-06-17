class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #We'd need some way to check that they are the same
        #And are going to need to iterate through them

        #Keep track of letters found in words
        s_dict = {} 
        t_dict = {}
        
        #Iterate through characters in string due to same length
        for c in range(len(s)):

            #Store character in dictionary found in every iteration
            s_dict[s[c]] = 1 + s_dict.get(s[c], 0)
            t_dict[t[c]] = 1 + t_dict.get(t[c], 0)

        #Then compare dictionaries to each other to see if dictionaries are the same, else return false.
        return s_dict == t_dict
