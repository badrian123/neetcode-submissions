class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        count = 0
        for i in nums:
            if (i-1) not in hash_set:
                after = i +1
                length = 1
                while after in hash_set:
                    after += 1
                    length += 1
                count = max(length, count)
        return count

