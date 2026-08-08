class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Going to need to store results in an array
        #Going to iterate through the values from left to right first but multiply everything except current index
        #Going to iterate through the values from right to left by multiplying everything except current index.
        #Should hopefully lead to result.

        res = [1] * len(nums)
        prefix, postfix = 1,1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res