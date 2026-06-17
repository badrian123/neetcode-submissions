class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Given a binary array.
        #Need to return the maximum number of consecutive 1's in the array.

        #It is going to be consecutive so that probably means that I will reset count when consecutive breaks.
        #I will also be keeping track of maximum consecutive throughout the entire process
        #Finally return the maximum consecutive count.

        count = 0
        max_consec = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_consec = max(count, max_consec)
                count = 0
        return max(max_consec, count)
