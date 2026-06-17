class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in range(len(nums)):
            elements[nums[n]] = 1 + elements.get(nums[n], 0)
        
        for key, value in elements.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for h in freq[i]:
                res.append(h)
                if len(res) == k:
                    return res

        