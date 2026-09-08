class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Need to return indices in 1 index form
        #Index values need to add up to target.

        #going to use a dictionary to keep track of what value has been seen and stored with its index
        #Going to use the difference between target and current value to find the second index.

        seen = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in seen:
                return [seen[diff]+1, i+1]
            seen[numbers[i]]=i
        