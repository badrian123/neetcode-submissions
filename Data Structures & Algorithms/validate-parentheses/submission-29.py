class Solution:
    def isValid(self, s: str) -> bool:
        #Need to create links.
        #Going to use a stack to keep track of what's been seen.
        #Going to check in the end if the stack is empty or not.
            #This will determine if we have processed everything or not.
        
        brackets = {
            "]":"[",
            ")":"(",
            "}":"{"
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

        return False if stack else True