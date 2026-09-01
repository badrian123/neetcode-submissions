class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Same characters
        #Same length.
        #In any order.
        #I would use two dictionaries in order to keep track of what characters have been seen from the string.
        #Then compare the two dictionaries against each other in order to see if they are equal or not.
            #If they are equal, then they anagrams b/c they have the same keys and values.
        
        #This works because it purely checking if two dictionaries are the same regardless of the strings order.
            #The dictionary will simply take care of what has been examined.

        #First need to check that both strings are of same length.    
        if len(s) != len(t):
            return False

        #Then proceed forward.
        s_dict, t_dict = {}, {}

        #Basically iterating through both strings, regardless of what character pops up.
            #Then, keeping track of it by storing the occurences that the character appears into the dictionary.
        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
        return s_dict == t_dict