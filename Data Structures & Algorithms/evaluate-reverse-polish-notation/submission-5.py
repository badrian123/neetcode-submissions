class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Input
            #Array of strings
        
        #Output
            #Return the integer that represents the evaluation of the expression.

        #Note to self:
            #Integers or the result of other operations
                #So might have to append result to stack possibly
            #Interesting.
            #So I know that I am going to have to iterate through the list of strings.
            #Then I am going to have to perform specific operations based on the operand string.
            #If it is just a number, I assume the number is just going to be stored in a stack.
            #I do need to keep in mind how I perform the operation or the operation order.
                #in order to prevent inaccurate results
            #Besides that, it seems that the result after the operation is stored back into the stack.

        nums = []
        for c in tokens:
            if c == "+":
                #I need two numbers so I will do two pops
                res = nums.pop() + nums.pop()
                nums.append(res)
            elif c == "-":
                a,b = nums.pop(), nums.pop()
                res = b - a
                nums.append(res)
            elif c == "/":
                a,b = nums.pop(), nums.pop()
                res = int(float(b) / a)
                nums.append(res)
            elif c == "*":
                res = nums.pop() * nums.pop()
                nums.append(res)
            else:
                nums.append(int(c))
        
        #The latest value should be at the front
        return nums[0]            
