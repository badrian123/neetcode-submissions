class Solution:

    def encode(self, strs: List[str]) -> str:
        #Need to iterate through a list of strings.
        #Somehow encode it.
            #I recall using the string length and the # in order to encode
            #This was all in one string and returned as one string.
        res = ""
        for s in strs:
            string_len = str(len(s))
            code = "#"
            res += string_len + code + s
        return res

    
    def decode(self, s: str) -> List[str]:
        #I recall iterating through the entire string but character by character
        #I recall there being a process to locate the code
            #Then once code found, I am able to extract the string length
        #Then reposition pointers, so left and right pointers are used.
        #Extract the string by appending it to an array
        #Then repeat process until end of string and return the array.
        
        res = []
        l, r = 0, 0
        while l < len(s): #Iteration
            while s[r] != "#": #Locate code
                r += 1
            string_len = int(s[l:r])
            l = r + 1 #After code
            r = l + string_len #After last character
            res.append(s[l:r]) #Add string to list
            l = r #Reposition l pointer to next starting position
        return res