class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypt = "#"
        encoded_string = ""
        for s in strs:
            string_length = str(len(s))
            encoded_string += string_length + encrypt + s
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        
        while l < len(s):
            while s[r] != "#":
                r += 1
            string_length = int(s[l:r])
            l = r + 1
            r = l + string_length
            res.append(s[l:r])
            l = r
        return res
    