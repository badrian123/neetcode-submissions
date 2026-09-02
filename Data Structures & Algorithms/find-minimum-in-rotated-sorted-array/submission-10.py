class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Note to self
            #Rotation can produce original array

        #Output 
            #return the minimum
        #Got to work with what I got
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            #Then going to be checking middle value to see if it is min value
                #This is the only spot we are checking our mins
            m= (l + r)//2
            res = min(res, nums[m])
            #Then working with what I got, in order to eliminate sections
                #so that I can save time in not needing to examine them.
            if nums[l] <= nums[m]:
                #Makes no sense to check 3,4,5 so moving l saves us that trouble / extra work
                l = m + 1
            else:
                r = m - 1
        return res

