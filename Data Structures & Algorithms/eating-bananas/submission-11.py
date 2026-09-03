class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #So I know to solve this is by figuring out a rate.
            #Testing the rate
            #Then adjusting the rate
        res = max(piles)
        low_e, high_e = 1, max(piles)
        while low_e <= high_e:
            rate = (low_e + high_e) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/rate)
            
            if hours <= h:
                res = rate
                high_e = rate -1
            else:
                low_e = rate + 1
        return res