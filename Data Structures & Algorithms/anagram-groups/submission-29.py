class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Group all anagrams together into sublists.
        #Ok. So for this problem, I need to find a way to group all anagrams together
            #into sublist. 
            #However, the characters are going to be random and so.
            #I need a way to identify them in order to know which are the same and which aren't the same.
        #Since the characters are going to be the same, they should form the same id.
        #Meaning, I know of a way where if I iterate through the string. Then go character by character in order
            #to create an id. All similar strings should have the same id.
        
        #What will I need?
            #defaultdict(list) -> b/c that's how I will store anagrams accordingly.
            #Two iterations, on for the string and one for the individual character.
            #A list called id, which will be used in order to create an id out of it.
        anagrams = defaultdict(list)

        for s in strs:
            id = [0] * 26
            for c in s:
                #Ord process should be able to generate an index that I can use to input a value into / at the id list
                id[ord(c) - ord("a")] += 1
            #Now I need to insert it to the dictionary. 
                #But the list is not immutable so going to need to make it into a tuple.
            anagrams[tuple(id)].append(s)
        
        return list(anagrams.values())
