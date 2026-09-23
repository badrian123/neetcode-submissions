class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #going to need to store the key and the value. So I am going to need a dictionary.
        #going to see if the difference is in the dictionary.
            #Based on that I will return the indices or add to the dictionary.
        
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
        