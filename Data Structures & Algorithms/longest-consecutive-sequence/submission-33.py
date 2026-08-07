class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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