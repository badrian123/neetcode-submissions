class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #So I know that I need to focus on the number that doesn't have anything before it.
        #I also need to check if numbers have been seen without having to iterate through the entire thing
        #I am going to need to use a set because insertion & search are O(1)
        res = 0
        seen = set(nums)

        for n in nums:
            #Making sure theirs no number before it
            if n - 1 in seen:
                continue
            
            length = 1
            while n + length in seen:
                length += 1
            res = max(length, res)
        
        return res