class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #I will need to organize the numbers.
        #I will need to count the occurences.
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Iterate through the numbers
        # Will i need the index or the number
        # The number because i am counting that.
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            freq[value].append(key)

        res = []
        for p in range(len(freq)-1,0,-1):
            for v in freq[p]:
                res.append(v)
                if len(res) == k:
                    return res
        return res