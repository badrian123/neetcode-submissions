class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I need to return the indices.
        #They need to add up to the target.

        #If I am going to be given a list.
            #I need some way to know what exists.

        #Dictionary. -Done
            #ahh. Ok.
            #So I am going to store what I have already used in the dictionary.
            #Then I am going to use the difference in order to see if it is in the dictionary.


        seen = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in seen:
                return [seen[diff], i]
            seen[v] = i

        #Will this work. Let's find out :)