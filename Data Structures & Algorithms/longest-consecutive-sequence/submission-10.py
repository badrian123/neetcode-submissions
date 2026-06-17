class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        seen = set(nums)
        for num in nums:
            one_greater = num + 1
            count = 1
            while True:
                if one_greater in seen:
                    count += 1
                    one_greater += 1
                else:
                    break
            res = max(res, count)
        return res