class Solution:

    def encode(self, strs: List[str]) -> str:
        #I am going to encode the string.
        #Use an identifier in order to know how long the string is
        #Hopefully leading to me being able to use those instructions in the encoded string to decode it.

        code = "#"
        encoded_string = ""

        for s in strs:
            string_len = str(len(s))
            encoded_string += string_len + code + s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        #Now, I need to identify the code
            #That will give me the length of the string.
            #It should also help me with positioning.
        
        #Seems like I am going to use two pointer approach too.
        res = []
        #Wait a minute.
            #Ok. So I am going to need to iterate through the string. -Done
            #I am also going to need to identify the code.
            #I am going to need to obtain the length of the string.
            #I am going to have to move my pointers positions in order to extract the string.
            #Finally store the extracted string into res, readjust position and repeat process until reach end of string.
        l, r = 0, 0
        while l < len(s)-1:
            #I am going to use the right pointer to find the code.
            while s[r] != "#":
                r += 1
                #Yea, that should help me search for the code because I need what between in order to extract.
            string_len = int(s[l:r])
            l = r + 1 #Don't want it to be on the code but on the first character.
            r = l + string_len #Want it to be one character after the string
            res.append(s[l:r]) #This should extract the string.
            l = r #Will need to adjust left pointer so process of finding next string can happen.
        
        return res

