class Solution:
    def findMin(self, nums: List[int]) -> int:
        #ok. So I need to return the minimum.
        #What I am thinking is to look at the middle value and then decide if i should
            #adjust up or down.
        #Basically, I will use the front and end in order to determine how to adjust

        #These are going to be my front and end

        l, r = 0, len(nums)-1
        minVal = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break

            #This gives me my middle index.
            m = (l+r) // 2
            minVal = min(minVal, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1                
        return minVal

            #Now with the middle, front and end I need to determine where to adjust.
            #What would happen if middle is greater than front?
                #That probably means I should check more to the right.
            #What will this all do?
                #This will give me hope for a direction.

            #Not to sure on this -> #What if middle is less than front?
                #likely to what we are looking for. IDK