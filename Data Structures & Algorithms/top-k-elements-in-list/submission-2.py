class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rankedNum = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            rankedNum[n] = 1 + rankedNum.get(n, 0)
        for key, value in rankedNum.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res