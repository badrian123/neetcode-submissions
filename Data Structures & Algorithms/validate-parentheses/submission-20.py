class Solution:
    def isValid(self, s: str) -> bool:
        #Going to need to specify bracket connections (Dictionary) in opposite order
        #Going to need to iterate through the list of strings character by character.
        #At every character, going to need to if it is a key of the bracket connection
            #Going to need to check if stack is empty.
            #Going to need to compare if last item in stack matches with current character.
                #If these two conditions are satisfied then pop out the last value in stack
                #Else:
                    #Return false
            #Else, I would add to a stack (Array)
        #Finally need to check if stack is empty.
            #So if it is, return True else False
        brackets = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False