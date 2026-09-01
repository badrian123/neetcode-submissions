class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        pending = []

        for i, v in enumerate(temperatures):
            while pending and pending[-1][1] < v:
                index, temp = pending.pop()
                res[index] = i - index

            pending.append((i,v))
        
        return res