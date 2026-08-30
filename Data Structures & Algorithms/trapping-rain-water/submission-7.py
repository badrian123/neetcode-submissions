class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        #For iteration purposes
        l, r = 0, len(height)-1
        #For direction purposes
        maxLeftHeight, maxRightHeight = height[l], height[r]

        while l < r: #Not sure if they need to cross but will find out
            #Determine direction.
            if maxLeftHeight <= maxRightHeight:
                l += 1
                maxLeftHeight = max(maxLeftHeight, height[l]) #In order to set the bigger number
                #This is just the water in between the two left heights.
                water = maxLeftHeight - height[l]
                res += water
                #That's really honestly that we are needing.
            else:
                r -= 1
                maxRightHeight = max(maxRightHeight, height[r])
                water = maxRightHeight - height[r]
                res += water
        return res