class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = set(nums)

        for n in nums:
            if n - 1 in seen:
                continue

            temp = 1
            j = n + 1

            while j in seen:
                temp += 1
                j += 1

            count = max(temp, count)

        return count