class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #I see that the shorter wall is used b/c if water was filled to to the brim, it would leak due to shorter height
        
        #I need to calculate the area
            #Width * Height
        #Going to use two pointer approach
        #Going to keep track of maxArea found.
        
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = height * width
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1        
            #Now, do I want to move both of my pointers or just one of them?
                #One of them is simply adjusting the width.
            #Both of them is shrinking the width twice as fast.

        return res

        #Why it didn't work.
            #The objective is to also try every single position possible.
            #By moving both pointers at the same time, I ended up not trying all possible combinations.
