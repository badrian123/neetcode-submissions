class Solution:

    def encode(self, strs: List[str]) -> str:
        #Going to basically create a string that should have internal instruction
            #on how to decode
        code = "#"
        encoded_string = ""
        for s in strs:
            string_len = str(len(s))
            encoded_string += string_len + code + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        #Going to take coded string, use instructions, to extract and store strings
        #in a list
        #To find the code: #
            #String Length
        #Extract string
        #Prepare for next string
        #until reached the end of the string.
        res = []
        l, r = 0, 0
        while l < len(s):
            #Need to find the code
            while s[r] != "#":
                r += 1
            #We found the code. So get the string length
            string_length = int(s[l:r])
            l = r + 1
            r = l + string_length
            res.append(s[l:r])
            l = r
        return res