class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        #Just keeping track of what's pending
        stack = []

        #Going to iterate through the temperatures.
        #Need to store the index, so I know where to store results, and temperature.
            #Tuple is going to be stored in stack.
        #Going to be checking if temp in stack is less than current iteration temp,
            #then do the logic
            #else just add to stack and continue iteration

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                diff = i - index
                res[index] = diff
            stack.append((i,t))
        
        return res