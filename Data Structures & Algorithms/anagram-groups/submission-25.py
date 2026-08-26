class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #I need a place to store the anagrams.
            #This place will have the anagrams sorted.
                #What would work best is a dictionary list
        #Store by an id, that will be used to store in dictionary with in list values
            #Id is with ord and array.

        anagrams = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c)-ord("a")] += 1
            anagrams[tuple(id)].append(s)
        return list(anagrams.values())
