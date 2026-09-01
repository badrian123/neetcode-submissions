class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #So multiplication of every value except itself.

        #I know the postfix and prefix approach.
        #Basically, going to multiply all values starting from left to right; except self.
            #This will be prefix.
        #Then we are going to multiply all values from right to left; except self.
        #In the end, we should end up with the requested output.

        #This is to help return our result.
        res = [1] * len(nums)
        prefix, postfix = 1, 1

        #Now, iteration from left to right
        for i in range(len(nums)):
            res[i] = prefix #Yes because we skip itself.
            prefix *= nums[i] #And multiply everything else.
        
        #Now, iteration from right to left.
        for j in range(len(nums)-1,-1,-1): #-1 in order to process the entire list completely.
            res[j] *= postfix
            postfix *= nums[j]
        
        return res