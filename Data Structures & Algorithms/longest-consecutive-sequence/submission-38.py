class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        #So going to insert list into set.
            #This is to help me identify if a value exists in the list.

        #Then going to iterate through the list
        #Going to check if there is a previous value,
            #because we don't want to count if we are not at the starting line.
        #The max count is going to be result.
        for v in nums:
            previousValue = v -1
            if previousValue in seen:
                continue
            
            length = 1
            while v + length in seen:
                length += 1
            res = max(res, length)
        return res