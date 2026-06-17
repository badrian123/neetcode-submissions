class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L, R = 0, len(height) -1
        maxLeftHeight, maxRightHeight = height[L], height[R]

        while L < R:
            if maxLeftHeight < maxRightHeight:
                L += 1
                maxLeftHeight = max(maxLeftHeight, height[L])
                res += maxLeftHeight - height[L]
            else:
                R -= 1
                maxRightHeight = max(maxRightHeight, height[R])
                res += maxRightHeight - height[R]
        return res