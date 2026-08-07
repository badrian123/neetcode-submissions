class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = set(nums)

        for n in nums:
            if n-1 in seen:
                continue
            
            length = 1
            while n + length in seen:
                length += 1
            count = max(length, count)
        return count