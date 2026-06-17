class Solution:
    def isValid(self, s: str) -> bool:
        #Have a hash map of what brackets belong to.

        #So I iterate through the string.

        #Store the open brackets into an array.
        
        #Once I encounter a closed bracket, I will pop the open bracket array, use it as a dictionary key, and compare value to current string.
            #If not matches I return false,
        #At the end of iteration, I return True.

        bracket_connect = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        stack = []
        for c in s:
            if c in bracket_connect:
                stack.append(c)
            else:
                if stack and bracket_connect[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
