class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c)-ord("a")] += 1
            group[tuple(id)].append(s)
        return list(group.values())
        
