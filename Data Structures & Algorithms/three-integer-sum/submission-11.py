class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Returning the values
        #No duplicates

        #Iterate
        #Efficiencies
            #Stop when value is possitive
            #Make sure that we aren't on a duplicate.
        #Going to use two pointer approach.
            #In order for it to work, need to have list sorted.
        
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i -1]:
                continue
            #i is on hold, and two pointer approach is going to be used here.

            l = i + 1
            r = len(nums)-1
            while l < r:
                sum = v + nums[l] + nums[r]
                
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res

