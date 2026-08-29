class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_e, high_e = 1, max(piles)
        res = max(piles)

        while low_e <= high_e:
            rate = (low_e + high_e) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(float(pile/rate))
            
            if hours <= h:
                res = rate
                high_e = rate - 1
            else:
                low_e = rate + 1
        
        return res