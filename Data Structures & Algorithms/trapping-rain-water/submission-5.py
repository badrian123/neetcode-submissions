class Solution:
    def trap(self, height: List[int]) -> int:
        #So I am going to need a variable in order to store my results.
        #I am going to use two pointer in order to solve this.
        #I will get the water amount based on the path that is selected.
        #using the max height, the height after it and then calculating the difference gives water result

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