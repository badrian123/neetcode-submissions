class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Going to need a dictionary that has values of arrays
        #Going to need to create an id that will help store the strings into their corresponding key
        #That way similar strings are in the same key location.

        anagrams = defaultdict(list)
        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c) - ord('a')] += 1
            anagrams[tuple(id)].append(s)
        
        return list(anagrams.values())