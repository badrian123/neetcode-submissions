class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = width * length
        #Going to use left and right pointer
        #Want to use the smallest height due to water spillage.

        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1 
           
        return res