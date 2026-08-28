class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #What do I remember
        #I know that results are going to be set initially to zero
        #I know that I am going to use a stack.
        #I knowq that I am going to be using the stack in order to check if the
            #current temperature is greater than what's in the stack.
        #If current iteration temp is greater then we will adjust results.
        #Else, we will add current iteration to stack for pending higher temp.

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                #Still need to update results even though we popped it from stack.
                res[stackIndex] = i - stackIndex
            stack.append((t,i))
        return res