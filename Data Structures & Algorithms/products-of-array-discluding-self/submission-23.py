class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Going to do some multiplication on the array,
            #starting from the left side all the way to the right.
            #Then I am going to do some multiplication from the right side
            #all the way back to the left / front of the array.
        #In each iteration, I am ignoring the current value for the current index
        #and only grabbing the current value for future references.

        res = [0] * len(nums)
        prefix, postfix = 1, 1


        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res