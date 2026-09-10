class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #Going to need to create some arrays.
        s1Count, s2Count = [0]*26, [0]*26
        #Going to create our first window
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord("a")] += 1
            s2Count[ord(s2[i])-ord("a")] += 1

        #Going to check our arrays against each other
        #Going to setup the sliding window
        #Going to start at len(s1), len(s2) because we already created our first window
        #Going to check if matches == 26 and return true
        #going to check our right and left pointers
        #Going to create our index based on s2
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r])-ord("a")
            s2Count[index] +=1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l])-ord("a")
            s2Count[index] -= 1
            if s1Count[index]==s2Count[index]:
                matches += 1
            elif s1Count[index]-1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
