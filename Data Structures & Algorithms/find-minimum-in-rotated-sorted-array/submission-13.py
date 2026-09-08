class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Output
            #need to find the minimum in the array.
        
        #I would use a binary search.
        #I would have to decide what direction to look.
        #whether it is left or right
            #Not given a target
            #So I am working with the values that I have.
            #Using the middle to always decide if I want to look left or right.
        l, r = 0, len(nums)-1
        res = float("inf")
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r)//2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return res