class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Conditions:
            #Space must be O(1)

        #Output
            #Are returning the index
                #needs to be in 1-indexed format
            #Needs to be two numbers that add up to given target
        
        #Can't use set()
        #I need to get to target.
        #Two pointer (This works because list is sorted)
            #Using both sides of the list.
            #Adding them together to create a sum.
            #Based on sum
                #If it is less than the target
                    #We move the left pointer up
                #Else
                    #Move right pointer down.
            #Goal is to check all value until we reach solution.
                #There will always bee a valid solution.        
        
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]
