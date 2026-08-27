class Solution:
    def isValid(self, s: str) -> bool:
        #Every open bracket is closed by the same type of close bracket
        #Correct order
        #Same type.

        #I know that I can use a dictionary in order to store correspondents.
        #I know that an array stack would be useful.
            #.pop() & .push()
        #I know that I am adding the bracket to the stack.
        #I need to keep in mind the stack being not empty
        #I need to keep in mind if the stack has something.
        #I need to keep in mind to check the last value in stack before popping.

        correspondents = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []
        for c in s:
            if c not in correspondents:
                stack.append(c)
            elif stack and stack[-1] == correspondents[c]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True