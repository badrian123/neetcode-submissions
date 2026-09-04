class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #I need to sort strings and keep similar strings together while everything else separate accordingly.
        #I need to identify and create an id off of the strings because the same id will be generated for
            #the strings that have the same characters.
        #Once an id is generated, it becomes easy for me to store the string along it's other similar strings.

        #To store strings
        anagrams = defaultdict(list)

        #Going to need to iterate through the list of strings.
        for s in strs:
            #Here is where I am going to need to create a id.
            id = [0] * 26
            for c in s:
                #now, this is what creates the id
                id[ord(c) - ord("a")] += 1
            #Now going to store the string based on the generated id.
            #I'd needs to be tuple because array isn't immutable.
            anagrams[tuple(id)].append(s)
        #It want's a 2d list so I'll put the results in it
        return list(anagrams.values())            