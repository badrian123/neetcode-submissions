class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least_eat, most_eat = 1, max(piles)
        res = most_eat

        while least_eat <= most_eat:
            mid_eat = (least_eat + most_eat) // 2

            total_eating_hours = 0
            for pile in piles:
                total_eating_hours += math.ceil(float(pile/mid_eat))
            
            if total_eating_hours <= h:
                res = mid_eat
                most_eat = mid_eat - 1
            else:
                least_eat = mid_eat + 1
        return res
    