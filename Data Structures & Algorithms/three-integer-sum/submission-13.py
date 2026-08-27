class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Nums needs to be sorted in order for left right pointer approach to work.
        #Going to use pointer to check value after the current position.
            #Much more of this will make sense when in iteration process.
        
        #For profeciencies in iteration
            #Going to break loop the moment value is greater than 0
            #Going to be checking prior value against current value in order to determine duplicate work.
        
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i -1]:
                continue
            
            l, r = i + 1, len(nums)-1
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