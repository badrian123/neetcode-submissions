class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Going to need to use a set.
        #Going to need to iterate through the list and see if it has been seen
        #Else, add the value to the set.

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False