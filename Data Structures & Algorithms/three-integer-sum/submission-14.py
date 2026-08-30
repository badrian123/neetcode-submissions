class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Need to sort list for two pointer to work. -Done
        #Need to save work at 'a' position.
        #Going to use enumerate for index and value.
        #Going to use two pointer approach.
            #Two pointer will be inside enumerate for loop.

        #Going to need a res variable to store results. -Done
        #Going to be checking for possible duplicate work in 'a' -Done
        # and during a solution is found
        
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            #If v is positive, it would be hard to get a zero result from positive numbers.
            if v > 0:
                break
            
            #Need to save duplicate work.
                #Scenarios where v is equal to the previous iteration.
                #That just leads to duplicate work.
            if i > 0 and v == nums[i-1]:
                #i > 0 is just so that second part of condition works.
                continue
            l,r = i + 1, len(nums)-1
            while l < r:
                sum = v + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    #Solution.
                    res.append([v, nums[l], nums[r]])
                    #Now need to save duplicate work & can still further check while in current situation.
                    #Makes no sense to leave left pointer at current position so will increment
                    l += 1
                    #Here's where I am going to further check and possibly save work.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res



