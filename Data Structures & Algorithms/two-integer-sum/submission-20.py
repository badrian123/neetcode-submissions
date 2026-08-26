class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Need a way to store what has already been seen.
        #Need to use stored seen nums in order to see if a value already exists in stored place.
        #That will help me return the values that i am looking for.

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
    
