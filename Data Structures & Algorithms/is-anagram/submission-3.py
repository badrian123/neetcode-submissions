class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1_count = {}
        s2_count = {}

        for i in s:
            if i not in s1_count:
                s1_count[i] = 1
            else:
                s1_count[i] += 1
        for j in t:
            if j not in s2_count:
                s2_count[j] = 1
            else:
                s2_count[j] += 1
        for h in s1_count:
            if h not in s2_count:
                return False
            if h in s2_count and s2_count[h] < s1_count[h]:
                return False
        for h in s2_count:
            if h not in s1_count:
                return False
            if h in s1_count and s1_count[h] < s2_count[h]:
                return False
        return True
