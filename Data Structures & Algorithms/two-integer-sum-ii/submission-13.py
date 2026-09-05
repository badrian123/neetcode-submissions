class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Need to remember what was seen.
        #Need to calculate the difference.
        #Need to return in 1 index form
        seen={}

        for i in range(len(numbers)):
            diff = target- numbers[i]
            if diff in seen:
                return [seen[diff]+1, i+1]
            seen[numbers[i]] = i