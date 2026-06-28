class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        #Involves not repeating process twice.
            #Once in begining and other at end.
        #Needs to get sorted too; the array.
        res = []
        num.sort()

        for i in range(len(num)):
            if i > 0 and num[i] == num[i -1]:
                continue

            l = i + 1
            r = len(num)-1
            while l < r:
                sum = num[i] + num[l] + num[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([num[i],num[l],num[r]])
                    l += 1
                    while num[l] == num[l-1] and l < r:
                        l += 1
        return res