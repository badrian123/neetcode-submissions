class Solution:

    def encode(self, strs: List[str]) -> str:
        #ok, I need to iterate through strings.
        #I need to implement a code to it.
        #I need to implement the string length too.
        #In the end, return an encode single string.
        res = ""
        code = "#"
        for s in strs:
            string_length = str(len(s))
            res += string_length + code + s
        return res

    def decode(self, s: str) -> List[str]:
        #Beautiful
        #Now I need to break down the encoded string.
        #I know that the important stuff I will need is the string length
        #I will also need to find the code.
            #Finding the code will give me the length.
        #I will use pointers.
        res = []
        l, r = 0, 0
        while l < len(s):
            #This is finding the code & getting the position
            while s[r] != "#":
                r += 1
            string_length = int(s[l:r])
            #Now need to move positions in order to extract the string
            l = r + 1 #First character
            r = l + string_length #past last character
            res.append(s[l:r]) #String
            l = r

        return res