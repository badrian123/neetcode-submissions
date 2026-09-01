class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #So I am going to need to return an output array that is the product of all the elemens of num except it's position
        res = [1] * len(nums)

        prefix, postfix = 1, 1

        #Iterate to the left, everything except current position
        #Storing results in an array.

        #Iterate from the right to left, everything except current position - I might be wrong on this part
        #Storing results in an array.
        #Once done, be able to return a list based on requested output.

        for i in range(len(nums)):
            res[i] = prefix #This skips it's current self
            prefix *= nums[i] #This is for the next iteration
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix #Well, first iteration is still skipped.
            postfix *= nums[j] #this is preparing for next iteration.
        
        return res
            
                