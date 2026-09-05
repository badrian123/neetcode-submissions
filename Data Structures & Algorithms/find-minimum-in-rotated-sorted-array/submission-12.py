class Solution:
    def findMin(self, nums: List[int]) -> int:
        #I am going to have to select where I am going to look.
        #Then I need to see if that section has my target or i will have to adjust.
        #From there I should be able to adjust and then check all until done with the list.
        #Hopefully return the min.

        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            #Select where to look.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) //2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return res