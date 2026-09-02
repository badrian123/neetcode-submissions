class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Output:
            #Need to find the minimum element of the array.
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2

            #I have the middle value. I need to decide which direction to focus on
                #because if the front is less than the middle,
                    #then there is no point in checking between front and middle.
            res = min(res, nums[m])
            if nums[0] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res            