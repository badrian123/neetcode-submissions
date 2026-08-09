class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Going to need to iterate through the list of strings.
        #Going to need to find a way to keep all similar anagrams together and in a list
        #I recall using the id method in order to generate an id for the string and match similar strings together.

        anagrams = defaultdict(list)

        for s in strs:

            id = [0] * 26

            for c in s:
                id[ord(c)-ord("a")] += 1
            anagrams[tuple(id)].append(s)
        
        return list(anagrams.values())