class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_seen = set()
        for num in nums:
            if num in num_seen:
                return True
            num_seen.add(num)
        return False
