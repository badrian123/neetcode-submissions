class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Need to return true or false based on if they are anagrams.
        #Same characters & same length

        #How would I solve this?
            #I would for sure need to check if both the strings are of the same size. -Done
            #I would use dictionaries in order to keep track of characters found. -Done
                #That way I can compare dictionaries to each other and see if they are anagrams
                #In the dictionary, just incrementing per letter.
                #I also think that is all.
        
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        return s_dict == t_dict