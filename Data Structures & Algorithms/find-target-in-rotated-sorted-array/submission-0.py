class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Wouldn't same algo apply here?

        #you have result - Done
            #Result set to -1 initially.
            #Going to keep track of index position.

        #Then left and right pointer - Done
        #At the end of the iteration would return output - Done

        #Would be mainly checking if target equals to current value.

        #How to determine where to look though?
            #Well, current value if it is less than target go said direction
            #So pointers positions will be getting updated then.
                #More specifically middle.

        #Got this right
        res = -1
        l, r = 0, len(nums)-1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            #until here.

            if nums[l] <= nums[middle]:
                if target > nums[middle] or target < nums[l]:
                    l = middle + 1
                else:
                    r = middle - 1
            else:
                if target < nums[middle] or target > nums[r]:
                    r = middle - 1
                else:
                    l = middle + 1
        return res