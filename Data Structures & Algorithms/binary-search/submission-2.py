class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #So i am given distinct integers
        #Sorted in ascending order
        #Need to find integer target and return it's index

        #I'm thinking of using the two pointer approach
        
        #Then a binary search in order to find the target.

        l, r = 0, len(nums)-1

        while l <= r:
            m = (r+l)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        