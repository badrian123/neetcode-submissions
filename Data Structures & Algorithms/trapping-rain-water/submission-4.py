class Solution:
    def trap(self, height: List[int]) -> int:
        #So we need the heights on both sides.
            #The shortest height is selected due to water spilling
            #The gap is the amount of water at the position being examined.
        #We need pointers to check all position in the list.
        water = 0
        l, r = 0, len(height)-1
        maxLeftHeight, maxRightHeight = height[l], height[r]

        while l < r:
            if maxLeftHeight <= maxRightHeight:
                l += 1
                maxLeftHeight = max(height[l], maxLeftHeight)
                water += maxLeftHeight - height[l]
            else:
                r -= 1
                maxRightHeight = max(height[r], maxRightHeight)
                water += maxRightHeight - height[r]
        return water