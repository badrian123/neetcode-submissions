class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        leftMaxHeight, rightMaxHeight = height[l], height[r]

        while l < r:
            if leftMaxHeight <= rightMaxHeight:
                l += 1
                leftMaxHeight = max(leftMaxHeight, height[l])
                res += leftMaxHeight - height[l]
            else:
                r -= 1
                rightMaxHeight = max(rightMaxHeight, height[r])
                res += rightMaxHeight - height[r]
    
        return res