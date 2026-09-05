class Solution:
    def isValid(self, s: str) -> bool:
        #I need to connect the brackets so that I know what is connected to what
        #I need to keep track of what I have seen already.
            #This track the order in which stuff came in and what is going to need to be popped out.
        
        brackets = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        stack = []

        for b in s:
            if b in brackets:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return False if stack else True