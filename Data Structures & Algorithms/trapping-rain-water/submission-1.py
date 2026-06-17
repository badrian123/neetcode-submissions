class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L, R = 0, len(height)-1
        leftMaxHeight, rightMaxHeight = height[L], height[R]

        while L < R:
            if leftMaxHeight <= rightMaxHeight:
                L += 1
                leftMaxHeight = max(leftMaxHeight, height[L])
                res += leftMaxHeight - height[L]
            else:
                R -= 1
                rightMaxHeight = max(rightMaxHeight, height[R])
                res += rightMaxHeight - height[R]

        return res
