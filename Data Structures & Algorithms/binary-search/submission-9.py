class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #So need to return index, else return -1 of index.
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
