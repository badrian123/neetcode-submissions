class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Going to use left and right pointer approach.
        #Going to add left value and right value to get a sum and compare it to the target.
        
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l+1, r+1]
