class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_one = {}
        dict_two = {}

        for i in range(len(s)):
            dict_one[s[i]] = 1 + dict_one.get(s[i], 0)
            dict_two[t[i]] = 1 + dict_two.get(t[i], 0)

        return dict_one == dict_two