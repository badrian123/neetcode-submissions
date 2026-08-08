class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        #I need to count how many times a number occurs and store that in a dictionary
        for n in nums:
            count[n] = 1 + count.get(n,0)
        #I need to then organize that info into an ordered structure
        for key, values in count.items():
            freq[values].append(key)
        
        #Finally I need to retrieve and store the values from order struvture into results.
        res = []
        for i in range(len(freq)-1,0,-1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res
        return res