class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkedNums={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in checkedNums:
                return [checkedNums[diff],i]
            checkedNums[nums[i]] = i
        return []