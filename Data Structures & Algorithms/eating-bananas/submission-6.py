class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_e, high_e = 1, max(piles)
        res = max(piles)

        while low_e <= high_e:
            rate = (low_e + high_e) // 2
            
            #Going to need to figure out the amount of hours that it takes based on the rate.
                #To eat the piles of course.
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/rate)
            
            #Need to adjust our rate based on it hitting target, doing better and worse.
            if hours <= h:
                res = rate
                high_e = rate - 1
            else:
                low_e = rate + 1
                
        
        return res