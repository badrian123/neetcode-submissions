class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []

        for c in s:
            if c in brackets:
                #Going to start checking stack to see if there are any open brackets
                #Also matching brackets to each other.
                #With order kept in mind.
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        #Now I just need to take care of the situation where stack still has brackets that need processing.
        return False if stack else True