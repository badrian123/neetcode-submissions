class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        res = []
        num.sort()

        for i, v in enumerate(num):
            if i > 0 and v == num[i -1]:
                continue
            L, R = i + 1, len(num)-1
            while L < R:
                threeSum = v + num[L] + num[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([v, num[L], num[R]])
                    L += 1
                    while num[L] == num[L -1] and L < R:
                        L += 1
        return res

