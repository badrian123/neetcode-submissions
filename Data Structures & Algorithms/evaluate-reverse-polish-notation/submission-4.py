class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #I know that I am going to be doing something with the operators.
        #Going to need to update the result
        #I remember popping two times

        stack = []
        for c in tokens:
            if c == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif c == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                res = int(float(b)/a)
                stack.append(res)
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                res = b - a
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[0]