class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Given integer array nums
            #of length n
        #Create an array ANS
            #of length 2n -so 2 times n ok
        
        #ans[i] == nums[i] -So matching values in same index position.
        #and[i+n] == nums[i] -So I am going to say that the values are just duplicated again.

        #Going to need an a array that I return
            #Going to need to make it twice the size of nums  
        #Then I iterate through the first nums array and insert the values into the new array.
        #Next I repeat the process for the further values
        #Finally I return the array.

        #So I got the first part down but, I am stuck a bit, on the second part.
        #So I can access the values from the nums array easily.

        new_array = [0] * (len(nums)*2)
        j = 0
        for i in range(len(new_array)):            
            if i == len(nums):
                j = 0
            new_array[i] = nums[j]
            j += 1
        return new_array
        

