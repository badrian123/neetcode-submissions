class Solution:
    def trap(self, height: List[int]) -> int:
        #Going to need to account for heights
        #The height difference is what gets me the water result
        #The two pointer approach is going to be used.
        #I need to get the heights at the front and back.

        res = 0
        l, r = 0, len(height)-1
        maxLeftHeight, maxRightHeight = height[l], height[r]

        while l < r:

            if maxLeftHeight <= maxRightHeight:
                l += 1
                maxLeftHeight = max(maxLeftHeight, height[l])
                res += maxLeftHeight - height[l]
            else:
                r -= 1
                maxRightHeight = max(maxRightHeight, height[r])
                res += maxRightHeight - height[r]
        return res

