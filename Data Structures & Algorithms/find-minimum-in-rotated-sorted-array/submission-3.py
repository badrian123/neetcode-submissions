class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] #First index stored as result.
        l,r = 0, len(nums)-1 #Grabbing both ends of the list.
        #So their no sorting.

        while l <= r: #Two pointer approach I guess.
            if nums[l] < nums[r]: #If left value is smaller than right value
                res = min(res, nums[l]) #Going to see if it is smaller than result due trying to find smallest num.
                break 
            #In a case where left value is not smallest.
                #The middle value is calculated.
            m = (l+r) // 2
            #Middle value is checked against result variable.
            res = min(res, nums[m])
            if nums[m] >= nums[l]: #Still middle is compared against left value.
                l = m + 1
            else: #Else, right value is decremented.
                r = m - 1
            #so it doesn't need to be sorted. Interesting.
        return res
