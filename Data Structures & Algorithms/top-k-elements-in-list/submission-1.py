class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checkedNums ={}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            checkedNums[n] = 1 + checkedNums.get(n, 0)
        for key, v in checkedNums.items():
            freq[v].append(key)
        print(freq)

        res =[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



