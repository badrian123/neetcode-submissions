class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            rate = (l + r) // 2

            #Now we need to calculate how long it takes to eat our piles at our rate
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/rate)
            
            #Now need to check our hours against the targeted hour

            if hours <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        return res