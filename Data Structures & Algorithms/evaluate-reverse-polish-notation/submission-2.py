class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #So basically there is always going to be two values in a stack.
        #Going to use conditions in order to determine the kind of operation to perform.
        #Going to store back the results in the stack so that it can be reused.
        
        stack = []
        for s in tokens:
            if s == "+":
                a, b = stack.pop(), stack.pop()
                sum = a + b
                stack.append(sum)
            elif s == "-":
                a, b = stack.pop(), stack.pop()
                diff = b - a
                stack.append(diff)
            elif s == "/":
                a, b = stack.pop(), stack.pop()
                div = int(float(b)/ a)

                stack.append(div)
            elif s == "*":
                a, b = stack.pop(), stack.pop()
                mult = a * b
                stack.append(mult)
            else:
                stack.append(int(s))
        
        return stack[0]