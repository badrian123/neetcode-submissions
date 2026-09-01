class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Value tripplets need to equal to zero
        #Can't have duplicate answers.

        #I will need to sort the list so that I can use two pointer approach -Done
        #I know that at some point, I would be wasting resource because I am trying to see if positive numbers equal to zero
            #Therefore, I need to account for this. -Done
        #Other than that, I am going to store my results in an array and return the output as a 2D array. -Done
        #I also need to account for when the current position is exactly the same amount of work as the prior iteration.
            #Therefore, I am going to need to account for this too. -Done




        #Where I am going to need to adjust my pointer position based on the sum.
        #Going to need to check for duplicate work in the while loop too.

        res = []
        nums.sort()
        #Wait, so I need three values not two so. I am going to need to set one value on hold while the two pointers
            #do it's work. -Done

        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and nums[i] == nums[i -1]:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                sum = v + nums[l]+nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    #Found our solution.
                    res.append([v, nums[l], nums[r]])
                    l+= 1
                    #Going to check for duplicate work and move our pointer until we get to work that hasn't been done before
                    while nums[l] == nums[l -1] and l < r:
                        l+= 1
        return res














