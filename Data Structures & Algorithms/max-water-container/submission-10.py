class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        #How am I going to get the max height?
        #I know that I have two pointer.
        #what am i going to do with the pointers?
        #I see, i still do the area but I move my pointers based on the height
        #Now, I need to decide where to loo

        l, r = 0, len(heights)-1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            res = max(res, area)

            #Now decide how to move my pointers
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res