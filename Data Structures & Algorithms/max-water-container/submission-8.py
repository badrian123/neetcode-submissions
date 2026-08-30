class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            #Now this is one check.
            width = r - l
            height = min(heights[l], heights[r]) #To account for water spillage
            area = width * height
            res = max(res, area)
            #Need to adjust in order to check other positions.
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
