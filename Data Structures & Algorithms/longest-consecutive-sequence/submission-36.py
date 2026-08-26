class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #I need to make sure that the element that's being examined, does not have a number before it.
        #Then I need to keep track of the biggest sequence counted.
        #Iterate until the end of the list.
        #Also, store all of the values in a set in order to do searches.

        res = 0
        seen = set(nums)

        for n in nums:
            if n - 1 in seen:
                continue
            
            length = 1
            while n + length in seen:
                length += 1
            res = max(length, res)
        return res