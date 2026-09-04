class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #So I have to return the most frequent elements
        #Also, I need to return how much is being requested.

        #So I have to count them in order to see how many there are.
        #Then with that information organize them in some order.
        #Finally, since the data is sorted, I will be able to simply go to area and extract until request done.

        #Going to use a dictionary because this will help me keep track of what's counted and results
        count = {}

        freq = [[] for i in range(len(nums)+1)] #The +1 is to account for zero count b/c can't count zero
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        #Now I need to organize the data.
        for num, appearance in count.items():
            #The order i am going to organize is based on occurence go to said spot.
            #So I need a 2d array.
            freq[appearance].append(num)
        
        #Now to extract amount being request and fulfill the request.
        res = []
        #I know the order is in ascending order where most appearances are at the end of the list
        #So I am going to focus there and then work backwards.
        for p in range(len(freq)-1, 0, -1):
            #Time to get the value
            for v in freq[p]:
                res.append(v)
                #Fulfill the requested amount
                if len(res) == k:
                    return res
