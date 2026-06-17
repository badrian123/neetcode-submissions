class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}

        for n in range(len(nums)):
            need = target - nums[n]
            if need in needed:
                return [needed[need], n]
            needed[nums[n]] = n
            