class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        
        for n in nums:
            if n-1 not in seen:
                length = 1
                j = n + 1
                while j in seen:
                    length += 1
                    j += 1
                res = max(res, length)
        return res
