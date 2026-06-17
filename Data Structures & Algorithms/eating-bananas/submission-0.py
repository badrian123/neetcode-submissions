class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_e, high_e = 1, max(piles)
        res = max(piles)

        while low_e <= high_e:
            k = (low_e + high_e) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile/k))

            if hours <= h:
                res = k
                high_e = k - 1
            else:
                low_e = k + 1

        return res
