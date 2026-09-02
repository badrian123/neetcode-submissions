class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        #I know that I am going to need to use a stack
        stack = [] #This is so that I can keep track of the heights found.
        #Do I know if I am going to use two pointer?
        #like why would i use l & r?
            #I don't think so.
            #I think this is where I use enumerate

        for i, h in enumerate(heights):
            #ok. This is good. Now, what exactly am I doing.
            #Well I am keeping track of the moment when I face a small height.
            #What's normal is that the the start is set to i at first.
            start = i
            #But then, we use a while loop in order to check for two conditions.
                #If there's anything in the stack
                #If there is, is the stack's height is bigger than the current height
                #Also, it's a while loop because we don't want to do this once.
                #We want to do this for the entire items in the stack.
            while stack and stack[-1][1] > h: #This is just because we faced a road block to the right
                index, height = stack.pop()
                #We need to do area calculations.
                maxArea = max(maxArea, height * (i - index))
                #makes sense, the current index is infront of the index that was stored in the stack.
                #now, the weird thing is that we set start to index
                #But this is just to inform that this is how further left we were able to extend before encountering a small height.
                start = index
            stack.append((start, h))
            #So this will help us out with uh the stacks in the iteration. Now what do we do about the stacks that haven't been processed?
            #Does it need to be in this for loop? No, it's it's own process.
        for i, h in stack: #I don't think i have to enumerate again b/c it'd be weird.
            #Still need to calculate the area for what's inside though.
            maxArea = max(maxArea, h * (len(heights)-i)) #The len of the array is to set a limit in it's expansion.
        return maxArea

        
