class Solution:
    def isValid(self, s: str) -> bool:
        #correct order of brackets closed
        #Brackets are linked to each other.
            #Meaning only specific brackets are able to close each other

        #What I need to do is link the brackets to each other.
            #That way I know what is linked to what
        
        #Then I need to keep track of the brackets that have been seen.
        #Next I need to develop a process in order to initiate the closing of brackets.

        #So I am going to use stacks. -Done
        #I am also going to use dictionary to link the brackets. -Done

        #This is formated in this way in order to help know when to initiate the closing of brackets process.
        brackets = {
            "]":"[",
            ")":"(",
            "}":"{"
        }

        track = [] #This will track what brackets have been seen. Mostly will have open brackets.

        for c in s:
            #What do I need to do here?
            if c in brackets:
                #start closing bracket process
                if track and track[-1] == brackets[c]:
                    track.pop()
                else:
                    return False
            else:
                track.append(c)

        #Finally check if all brackets are closed or if there are still some remaining
        return False if track else True

