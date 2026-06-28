class Solution:
    def trap(self, height: List[int]) -> int:
        #l, r pointers
        #res
        #maxLeftHeight and maxRightHeight
        
        res = 0
        l, r = 0, len(height)-1
        maxLeftHeight, maxRightHeight = height[l], height[r]

        while l < r:
            if maxLeftHeight <= maxRightHeight:
                l += 1
                maxLeftHeight = max(height[l], maxLeftHeight)
                res += maxLeftHeight - height[l]
            else:
                r -= 1
                maxRightHeight = max(height[r], maxRightHeight)
                res += maxRightHeight - height[r]
        return res

