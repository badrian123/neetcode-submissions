class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        #Remove all occurrence in nums in-place
        # nums[:] = []
        #Then return the number of elements in nums which are not equal to val

        """
        I will iterate through the array.
        I will check if the number equals to the val being removed.
        If it doesn't, I will add the value to another array that will be used for the in-place part
        Then I will get the length of the newely array and return that value.
        """
        res = []
        for num in nums:
            if num != val:
                res.append(num)
        nums[:] = res
        return len(res)