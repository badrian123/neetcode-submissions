class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1_hash = {}
        s2_hash = {}

        for s1 in s:
            if s1 not in s1_hash:
                s1_hash[s1] = s.count(s1)
        for s2 in t:
            if s2 not in s2_hash:
                s2_hash[s2] = t.count(s2)
        if len(s1_hash) < len(s2_hash):
            return False

        for s1 in s1_hash:
            if s1 in s2_hash and s1_hash[s1] < s2_hash[s1]:
                return False
            if s1 not in s2_hash:
                return False

        for s2 in s2_hash:
            if s2 in s1_hash and s2_hash[s2] < s1_hash[s2]:
                return False
            if s2 not in s1_hash:
                return False
        return True
