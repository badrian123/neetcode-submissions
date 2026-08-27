class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Looks like a square
        #The area is width * height
        #Going to use two pointer approach
        #Going to need to determine how I increment left pointer or right pointer based on height.
        #Width = r - l
        #Height needs to be smallest in order to account for water spillage.
        
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            width = r -l
            height = min(heights[l], heights[r])
            area = width * height
            res = max(res, area)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res