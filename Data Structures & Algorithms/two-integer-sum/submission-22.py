class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I'm going to use a dictionary to keep track of what's been seen
            #And store it's index position in the list
        
        #I am going to use the difference between the target and nums value to get
            #the second index
        
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]]=i
        