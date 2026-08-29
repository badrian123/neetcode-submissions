class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #So I need to keep matching anagrams together and return it.

        #I am going to have a list of them though. -Done
            #So I know that defaultdict(list) would help in sorting & keeping anagrams sorted. -Done

        #Issue:
            #I will need to find a way to make sure anagrams are being stored in correct dict key.
            #Solution:
                #I just need to create an id out of the anagrams since same anagrams should create same id.
        
        res = defaultdict(list)
        #So iteration of the string and create an id with the character.
        for s in strs:
            id = [0] * 26
            for c in s:
                id[ord(c)- ord("a")] += 1
            
            #So I have the id, now I need to make it so dict accepts it.
            res[tuple(id)].append(s) #This is a dictionary with list as a value.
        
        return list(res.values())

