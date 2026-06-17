class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Remove all occurrences of val in nums IN-PLACE
        #Return the number of elements in nums which are not equal to val

        #Going to need to iterate through the array.
        #Check if the current value is equal to val
            #Remove it if it is.
                #Or simply don't add it to an array that I am creating.
        
        new_array = []
        for i in range(len(nums)):
            if nums[i] != val:
                new_array.append(nums[i])
        nums[:] = new_array
        return len(new_array)