class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_seen = set()
        for num in nums:
            if num in num_seen:
                return True
            num_seen.add(num)
        return False

#Going to take O(n)
#Memory is going to take potentially up to o(n)