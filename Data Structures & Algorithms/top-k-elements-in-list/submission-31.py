class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Need to count.
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        #Need to count.
        for num in nums:
            count[num] = 1 + count.get(num,0 )

        #Need to organize.
        for num, oc in count.items():
            freq[oc].append(num)
        
        #Need to extract.
        res = []

        for p in range(len(freq)-1, 0, -1):
            for v in freq[p]:
                res.append(v)
                if len(res) == k:
                    return res
        return res
