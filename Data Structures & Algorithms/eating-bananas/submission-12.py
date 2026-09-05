class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #So I need to figure out a rate.
        #I know that I can eat, 1 banana and the max pile in piles
        #I am going to use the average of these to in order to create a rate.
        #Then I am going to get an amount of time it is going to take me to finish the piles at the rate.
        #Update res and adjust based on the amount of hours I took to eat the piles at the rate

        l,r = 1, max(piles)
        res = 0

        while l <= r:
            rate = (l+r)//2

            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/rate)
            
            if hours <= h:
                res = rate
                r = rate - 1                
            else:
                l = rate + 1
        return res