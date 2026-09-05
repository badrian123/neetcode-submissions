class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Going to have to decide what section to look.
            #Then if I am going to look further in that section.
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
