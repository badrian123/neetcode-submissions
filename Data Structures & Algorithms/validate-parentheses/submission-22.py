class Solution:
    def isValid(self, s: str) -> bool:
        #Going to need stack.
        #Going to need a dictionary in order to store bracket assignment.
        #Going to need to check if stack is empty and if last value matches dictionary value

        brackets = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []

        for c in s:
            if c not in brackets:
                stack.append(c)
            elif stack and stack[-1] == brackets[c]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False

