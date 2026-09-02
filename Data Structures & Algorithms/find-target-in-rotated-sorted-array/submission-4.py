class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        res = -1

        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m
            
            #Need to pick a side
            if nums[l] <= nums[m]:
                #Need to find a way not to go to the left section
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return res