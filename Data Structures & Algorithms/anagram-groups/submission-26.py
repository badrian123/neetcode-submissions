class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Going to need to store anagrams in a default dictionary list.
        #Going to need to create a id for the strings so that they are labeled and then stored together.
        #Going to use ord
        
        anagrams = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c) - ord("a")] += 1
            anagrams[tuple(id)].append(s)
        
        return list(anagrams.values())

