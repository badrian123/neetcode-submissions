class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #So I am going to need a way to count the occurences a number appears in the list. - Done
            #Going to use a dictionary for this. -Done
        
        #Then going to need to organize the numbers based on how frequent they appeared.
            #Going to use a 2D array for this.
        #After that, going to need to obtain the top most frequent values based on how much is being requested
        #And return it.

        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        #So I counted the amount of occurences
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        #Now I am going to organize it into the 2D array.
        for key, value in count.items():
            #This will store based on occurences and will have the numbers of similar occurences in the same list.
            freq[value].append(key)
        
        for p in range(len(freq)-1, 0,-1):
            for v in freq[p]:
                res.append(v)
                if len(res) == k:
                    return res
        return res