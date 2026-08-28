class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #In order to track days until a higher temp found
        stack = [] #In order to remember the days that still need to be checked for a higher temperature.

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop() 
                res[stackIndex] = i - stackIndex
            stack.append((t,i)) #In order to keep checking all of the days, so we are like adding it to a que but more like a stack.
        return res