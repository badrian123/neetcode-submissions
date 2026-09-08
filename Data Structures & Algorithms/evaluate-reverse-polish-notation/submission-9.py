class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Going to have to iterate through the strings in the array.
        
        stack = []
        for v in tokens:
            if v == "+":
                a,b = stack.pop(), stack.pop()
                sum = a + b
                stack.append(sum)
            elif v == "-":
                a,b = stack.pop(), stack.pop()
                sum = b-a
                stack.append(sum)
            elif v == "*":
                a,b = stack.pop(), stack.pop()
                sum = a * b
                stack.append(sum)
            elif v == "/":
                a,b = stack.pop(), stack.pop()
                sum = int(float(b)/a)
                stack.append(sum)
            else:
                stack.append(int(v))
        return stack[0]