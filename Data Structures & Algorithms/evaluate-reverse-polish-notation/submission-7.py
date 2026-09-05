class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #This one, I am using the operand.
        #I need to be careful in how i do operations for - and /
        #I need to store result back into stack.
        #I need a stack.
        stack = []

        for v in tokens:
            if v == "+":
                #I will need at least two pops
                a,b = stack.pop(), stack.pop()
                sum = a + b
                stack.append(sum)
            elif v == "-":
                a,b = stack.pop(), stack.pop()
                sum = b - a
                stack.append(sum)
            elif v == "*":
                a,b = stack.pop(), stack.pop()
                sum = a * b
                stack.append(sum)
            elif v == "/":
                a,b = stack.pop(), stack.pop()
                sum = float(b) / a
                stack.append(int(sum))
            else:
                stack.append(int(v))
        return stack[0]
