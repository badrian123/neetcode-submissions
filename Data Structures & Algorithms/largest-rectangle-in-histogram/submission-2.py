class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Will keep track of our area.
        maxArea = 0
        #Will store sections that will need to be processed for area calculation.
        stack = []

        for i, h in enumerate(heights):

            #Apparently going to have a start variable.
            start = i

            #While the stack has something stored and
                #the last value inserted height is greater than the iteration height.
                #we will do the following
            while stack and stack[-1][1] > h:
                #Pop out the last value inserted to the stack
                index, height = stack.pop()

                #calculate the area and check if it is the max area found
                width = i - index #So the current index minus the index stored
                maxArea = max(maxArea, height * width)
                #This part i find confusing.
                start = index
                #We'd keep iterating in the while loop until the height in the stack is
                    #no longer taller than the current iteration height.
            
            #Interesting part is we'd store either the current index to the stack or
                #the index that was popped out in the while loop.
                #The index that is set to start is simply tracking the first moment when,
                    #there was a shorter height and so that index position keeps being used
                    #because it lays out how far we can expand our width before encounter a wall
                    #that is too small. So all of this is done so that we don't calculate our area 
                    #wrong.
                    #They do call this expansion and are trying to see how far we can expand our width
                    #before encountering a shorter wall b/c our area wouldn't be correct if we expanded
                    #past it and did an area that tried to include space that isn't there.
            stack.append((start, h))

            #This is calculating the area for items still in the stack.
            #Interesting part about this is that it, uses the length of the list minus
                #whatever index it had stored. I recall that the reason, don't rely on this,
                #is to account for sections of the box that haven't been taken into account.
                #But I don't know. I guess.            
        for i, h in stack:
            listLen = len(heights)
            maxArea = max(maxArea, h * (listLen - i))
        return maxArea
