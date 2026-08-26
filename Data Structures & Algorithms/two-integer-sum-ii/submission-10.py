class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #So going to need to use two pointers for this.
            #Basically left and right positions, adding them together to get a sum.
            #Then with the sum, seeing if it is greater or less than target will determine which pointer to move
            #Until a solution is found and returned.
    
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]
        