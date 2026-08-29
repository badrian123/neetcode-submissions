class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #I know that I am going to be using stack in order to keep track of the days that need days counted
        #Going to use the index and temp
        #Going to need to set res initially to zero and as an array.

        #Layout done
        res = [0] * len(temperatures)
        stack = []

        #Enumeration needed
        for i, t in enumerate(temperatures):
            #So it's a while instead of an if because it needs to check the other stack values if the current t is greater too
            while stack and t > stack[-1][1]: #Right so i used tuple
                #Need to update res here
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = i - stackIndex #This does the math for days since a higher temperature stuff.
            #On first iteration, i am going to add to stack no matter what
                #In tuple format because index and temperature are both needed
            stack.append((i,t))
        return res


