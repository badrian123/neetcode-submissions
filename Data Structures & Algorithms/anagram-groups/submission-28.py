class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Going to use defaultdict(list) in order to
            #Store and separate anagrams. 
            #We only want similar anagrams to be in the same place.

        #Going to iterate through the strs.
            #Then iterate through the string's character.
            #Going to need to create an id in order to identify & label similar anagrams
            #Going to use an array with 26 zeros b/c there are 26 english letters
                #This part is what's going to help form the id.
        
        res = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c) - ord("a")] += 1
            res[tuple(id)].append(s)
        return list(res.values())