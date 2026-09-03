class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #This is basically only moving the right pointer while the left pointer stays put unless
            #some condition causes it to move.

        #Look at how the pointer positions are close to each other and not in either ends.
        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, (prices[r]-prices[l]))
            else:
                l = r
            r += 1
        return res