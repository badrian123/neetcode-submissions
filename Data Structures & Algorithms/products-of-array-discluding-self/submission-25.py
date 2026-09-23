class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prefix, postfix = 1, 1,

        #We need to iterate to the right.
        #Then iterate to the left.
        #Going to need the index

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res