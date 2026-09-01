class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Longest consecutive sequence of elements that can be formed.
        #O(n) time so no sorting b/c o(n log n)

        #I will need to store the list in a set because insertion is o(1)
        #So, I will need to iterate the list from the start.
        #Then I am going to see if the current value minus one exists in the set.
            #Why:
                #Because we don't want to start counting when there maybe a chance of a number missed.
                #Therefore, start counting when there aren't any numbers before it.
        res = 0
        num = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 in num:
                continue

            length = 1
            while (nums[i]+length) in num:
                length += 1
            res = max(res, length)
        return res