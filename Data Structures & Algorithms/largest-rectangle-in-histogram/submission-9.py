class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                area = width * height
                res = max(res, area)
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            width = len(heights) - i
            area = h * width
            res = max(res, area)
        
        return res