class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        top_k = []
        for id, key in enumerate(frequency):
            top_k.append([frequency[key],key])
        top_k = sorted(top_k)
        res = []
        for i in range(k):
            res.append(top_k[((i+1)*-1)][1])
        return res