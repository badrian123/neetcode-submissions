class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #So we are keeping track of the days when it was hotter.
        res = [0]*len(temperatures)
        stack = []
        #I am going to need to iterate through the temperatures
        #This is going to be based on if there is a temperature higher.
        #Going to need to keep track of index and temperature

        for i, t in enumerate(temperatures):

            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                days = i - index
                res[index] = days
            
            stack.append((i,t))
        
        return res