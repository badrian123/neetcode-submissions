class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #If a value appears more than once in the array.
        #So going to use a set in order to keep track of the values that have already been seen.
        seen = set()

        #Going to iterate through the array, and check every value if it has been seen in
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False