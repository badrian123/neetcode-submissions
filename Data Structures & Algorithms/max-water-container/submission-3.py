class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Area
        #Width
        #Height
            #Smallest Height
        #L, R pointers
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
        
        return res