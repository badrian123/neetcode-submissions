class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #It want's me to return the most frequent elements based on how many is being requested.
        #I am going to be given a list.
            #From the looks of the list, I am going to need to organize it.
            #Also figure out what is most frequent and how frequent the numbers are for each number.
        
        
        #One way I know how to do this is by
            #Counting the occurences that number appears in the list. 
                #This will give me at least their frequency for that number.
            #Next thing I will need to do is organize the count so that they are sort from lowest to highest frequency.
                #This will make it easier for me to know what numbers are the most frequent and where they are at.
                    #I am going to use a 2D array for this in order to organize the numbers based on most frequent.
            #The last part would be retrieving the requested amount back.
                #Since the frequency is already organized and sorted, 
                #it will be as simple as retrieving the end values because that's where the most frequent are at.
                #I will only need to return the amount that's being requested in order to fulfill the request.

        #Count
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #Freq organize
        freq = [[] for i in range(len(nums)+1)]
        for num, f in count.items():
            freq[f].append(num)
        #Return requested top frequent elements
        res = []
        #Highest should be at the end soo iterate from back to front.
        for p in range(len(freq)-1, 0, -1):
            for v in freq[p]:
                res.append(v)
                if len(res) == k:
                    return res
        return res