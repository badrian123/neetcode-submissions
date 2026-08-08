class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #So I am going to iterate through the list.
            #An easy way to check for duplicates is to keep track of what was already seen
                #So I use a set to keep track since insertion is O(1) and checking is O(1)
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False