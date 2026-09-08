class Solution:
    def trap(self, height: List[int]) -> int:
        #Need to determine where to look.
        #Then determine how much water is in that gap.
        #Then adjust where we are going to look next.
        res = 0
        l, r = 0, len(height)-1
        maxLeftHeight, maxRightHeight = height[l], height[r]

        while l < r:
            if maxLeftHeight <= maxRightHeight:
                #Look at the left area
                l += 1
                maxLeftHeight = max(height[l], maxLeftHeight)
                water = maxLeftHeight - height[l]
                res += water
            else:
                #Look at the right area
                r -= 1
                maxRightHeight = max(height[r], maxRightHeight)
                water = maxRightHeight - height[r]
                res += water
            
        return res