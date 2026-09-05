class Solution:
    def trap(self, height: List[int]) -> int:
        #I am going to use the heights on both side.
        #Which ever one is moved, I calculate the water in it.
        #at the end, I should have a sum

        res = 0
        l, r = 0, len(height)-1
        leftHeight, rightHeight = height[l], height[r]

        while l < r:
            if leftHeight <= rightHeight:
                #Now I need to get the water in here.
                l += 1
                leftHeight = max(leftHeight, height[l])
                water = leftHeight - height[l]
                res += water                
            else:
                r -= 1
                rightHeight = max(rightHeight, height[r])
                water = rightHeight - height[r]
                res += water
        return res