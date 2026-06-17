class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #returning the maximum number of consecutive 1's in the array.
            #Not, the amount of ones.
        #Well, I can use a for loop to iterate through the array.
            #Then, I have a variable that will keep track of the count.
            #I will, I will have a variable that stores the max consecutive at the moment.

            #So two variables.
            #I see that the count resets to zero when number isn't 1 so i will check what is max count and then restart count.
        
        max_consec = 0
        count = 0
        for num in nums:
            if num == 0:
                max_consec = max(max_consec, count)
                count = 0
            else:
                count += 1
            
        return max(max_consec, count)