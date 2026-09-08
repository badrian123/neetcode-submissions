class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #I know that I am going to have to iterate through the list.
        #What am i going to be doing though?
        #I need to look out for small heights in the left and right.
        #So as I am iterating to the right, I am going to be
            #Storing 
    
        #First iteration will store the (index, height)
        #Second iteration will check if current height is smaller than the height in the stack.
        #If it is, we are going to pop what's in the stack.
        #Then keep track of where the smallest height occured.

        #maxArea
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                area = width * height
                res = max(res, area)
                start = index
            stack.append((start, h))

        #Now I need to check the stack that have pending elements
        for i, h in stack:
            width = len(heights) - i
            area = h * width
            res = max(res,area)
        
        return res