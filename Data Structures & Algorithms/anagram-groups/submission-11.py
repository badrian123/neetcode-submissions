class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c)-ord("a")] += 1
            anagrams[tuple(id)].append(s)

        return list(anagrams.values())
