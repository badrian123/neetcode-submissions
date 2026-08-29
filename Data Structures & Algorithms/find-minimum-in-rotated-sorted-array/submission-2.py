class Solution:
    def findMin(self, nums: List[int]) -> int:
        #I would have to sort in order to then be able to use binary search to find the min.
        #Once sorted, I'd just use binary search and return the min.
        #sorting is logn i believe so still good.
        nums.sort()
        l, r = 0, len(nums)-1
        res = nums[0]
        return res
        # while l <= r:
        #     middle = (l + r) // 2

        #     if 