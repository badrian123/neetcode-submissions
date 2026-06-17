class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #So I am going to iterate through the list of strings
        #Then I am going to examine each string and appropriately apply the logic to the stack.
        #From there, I am going to sum up the stack and return that as the result.
        stack = []
        for ops in operations:
            #Going to use if conditions.
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops == "D":
                stack.append(2 *stack[-1])
            elif ops == "C":
                stack.pop()
            else:
                stack.append(int(ops))
        return sum(stack)


