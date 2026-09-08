class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Going to use a set in order to track what has been seen.
        #Going to store what has been seen in the set

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False