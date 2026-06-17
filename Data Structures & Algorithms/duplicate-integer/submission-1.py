class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_already_checked = {}
        for num in nums:
            if num in nums_already_checked:
                return True
            nums_already_checked[num] = 1
        return False
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False