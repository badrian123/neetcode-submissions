class Solution:
    def isValid(self, s: str) -> bool:
        #So I know I am going to need to a dictionary in order to specify what brackets connect to what
        #Going to need a stack in order to track what brackets have been added.
        #Going to need to check if stack is empty in the end.

        brackets = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        stack = []

        for c in s:
            #So I am going to iterate through the string.
            #What am I looking to do?
                #I need to see if it is a key of the bracket or needs to be added to stack.
                #Then check if brackets match with what's in stack or not.
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False            
            else:
                stack.append(c)      

        return False if stack else True