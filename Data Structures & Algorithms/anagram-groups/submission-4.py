class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c)-ord("a")] += 1
            grouped_anagrams[tuple(id)].append(s)
        return list(grouped_anagrams.values())
        