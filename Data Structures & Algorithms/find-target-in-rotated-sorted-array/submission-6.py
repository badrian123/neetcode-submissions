class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #So the way this solution works is by using what you have
            #in order to determine where to look
            #and potentially find the target in that direction.

        #The goal is to return the index that is the target that we are looking for.
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2

            #This is how well return our result.
            if target == nums[m]:
                return m

            #So at this point I have my setup, I just now need to decide where to focus my
            #attention on based on what I have.
            #What do I have?
                #So I have the front, middle and the end.
                #It's just common to check the left against the middle.
            #Either we are going to choose left or right.
            if nums[l] <= nums[m]:
                #Check our target if we should continue checking in this area.
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1 #worse case scenario