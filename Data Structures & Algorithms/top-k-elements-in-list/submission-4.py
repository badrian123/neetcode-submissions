class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #So I will need to store my counts and my results
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        #count the occurances
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num,v in count.items():
            freq[v].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

