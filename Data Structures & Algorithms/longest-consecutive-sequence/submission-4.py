class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #So what I can do is iterate through the list and add it to a hash set
        hash_set = sorted(set(nums))
        print(hash_set)
        count = 0
        if len(nums) != 0:
            count += 1
            tmp_count = 1
            for v in hash_set:
                num_one_greater = v + 1
                if num_one_greater in hash_set:
                    tmp_count += 1
                    if tmp_count > count:
                        count = tmp_count
                elif num_one_greater not in hash_set:
                    if tmp_count > count:
                        count = tmp_count
                    tmp_count = 1
            return count
        return count
