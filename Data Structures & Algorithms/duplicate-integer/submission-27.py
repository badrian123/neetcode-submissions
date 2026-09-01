class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Going to need to keep track of what has been seen.
        #Going to use a set.
        #Every iteration, I will be checking if the current value has already been seen.
            #If yes, then return True.
        #If reach the end of the iteration without finding duplicates,return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False