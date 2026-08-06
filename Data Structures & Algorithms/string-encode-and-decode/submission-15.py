class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            string_len = str(len(s))
            code = "#"
            res += string_len + code + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0,0
        while l < len(s):
            while s[r] != "#":
                r += 1
            string_len = int(s[l:r])
            l = r + 1
            r = l + string_len
            res.append(s[l:r])
            l=r
        return res