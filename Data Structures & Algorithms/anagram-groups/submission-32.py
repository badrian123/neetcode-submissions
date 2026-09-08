class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #I am going to create some form of id for the strings.
        #because the same string's should generate the same id.
        #This should help me keep similar strings together and the rest
        #organized accordingly.

        anagrams = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c)-ord('a')] += 1
            anagrams[tuple(id)].append(s)
        
        return list(anagrams.values())