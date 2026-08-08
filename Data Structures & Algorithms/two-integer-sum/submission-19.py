class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #I need to keep track of indice positions not just nums seen.
            #A dictionary helped with this.
        #To get the pair, I would need to get the difference.
            #With the difference, I can see if the number has already been seen that will add up to target.
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]]=i
