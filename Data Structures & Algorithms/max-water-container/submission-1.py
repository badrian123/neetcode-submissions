class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        L, R = 0, len(heights) -1

        while L <= R:
            width = R - L
            height = min(heights[L], heights[R])
            area = width * height
            res = max(res, area)

            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return res




