class Solution:
    def isValid(self, s: str) -> bool:
        #Going to need to use stack.
        #Going to need to use dictionary in order to know what is connected to what
        #Going to need to check if the stack is empty or has a value
        
        stack = []
        brackets = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        #Ok. Going to iterate through the string.
        for c in s:
            #I am going to need to see if the character is a key of dictionary brackets:
                #If it is then that means that it does not need to be stored but checked.
                #If it isn't part of the dictionary then it needs to be stored in the stack
            if c not in brackets:
                stack.append(c)
            else:
                #Check if stack isn't empty
                #Check if it matches to last value in stack array.
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else: #No point in popping due to not matching.
                    return False

        #Checks if stack is empty 
        if stack:
            return False
        else:
            return True