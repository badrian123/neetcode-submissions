class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_results = {}
        freq = [[] for num in range(len(nums)+1)]

        for num in nums:
            count_results[num] = 1 + count_results.get(num, 0)
        
        for key, value in count_results.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1, 0,-1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res