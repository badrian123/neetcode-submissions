class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for num in range(len(nums)+1)]

        #Iterate through the list and update count when number is found.
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        #So this will inverse the count and store the key in the array.
        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        