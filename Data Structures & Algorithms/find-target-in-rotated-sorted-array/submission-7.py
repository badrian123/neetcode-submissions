class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #So we are looking for our target, how am i going to go about this?
            #What do I got?
            #I got the middle value.
            #I got the target.
            #I got the front
            #I got the back.
            #What how am i going to isolate what I am looking for?
            #Well I can check either side but primarily the left side.
                #Because if it isn't in the left side then we check the right.
            
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            #Else, we need to check the left side

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                #Check right side
                if target < nums[m] or target > nums[r]:
                    r = m -1
                else:
                    l = m + 1
        return -1