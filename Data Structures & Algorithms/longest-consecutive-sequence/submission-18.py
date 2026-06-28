class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num = set(nums)

        for n in nums:
            if (n -1 ) not in num:
                length = 1
                while (n + length) in num:
                    length += 1
                res = max(res, length)
        return res 