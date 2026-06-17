class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate through the list of strings.
        #what strings belong together.
        #generate some kind of key, that will be used to insert the value into a dictionary.
        #going to need dictionary.
        #going to need some way to generate the key.
            #use an array to generate the key.
            #unicode pointer number function
                #converts a character into it's unicode number

        anagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            anagrams[tuple(key)].append(s)
        return list(anagrams.values())
     



