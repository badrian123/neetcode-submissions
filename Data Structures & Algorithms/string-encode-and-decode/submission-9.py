class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "#" + s
        return encoded_s

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []

        while l < len(s):
            while s[r] != "#":
                r += 1
            string_length = int(s[l:r])
            l = r + 1
            r = l + string_length
            string = s[l:r]
            res.append(string)
            l = r
        return res