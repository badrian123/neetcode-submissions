class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #I know i need to sort the array.
            #That will help me with positive number.
        #Then i need to keep track of duplicate work.

        res = []
        nums.sort()

        for i, v in enumerate(nums):
            #Don't want to do work on positive numbers.
            if v > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue

            #Two pointer
            l, r = i+1, len(nums)-1
            while l < r:
                sum = v + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    #need to do a further check for duplicate work.
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
        return res