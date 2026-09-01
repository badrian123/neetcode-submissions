class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Number of days after day a warmer temperature appears.
        #So I am checking to see if I can find a day that is warmer, if so, count how many days it's been since it has gotten 
            #warmer.
        
        #If no warmer day, then set to zero

        #I know that I am going to have to use a stack
            #In order to keep track of days that are being checked for a warmer day.
        #Then I am going to be comparing that stack with the current day.
        #My results will be stored in a array.
        
        res = [0] * len(temperatures)
        pending = []

        for i, v in enumerate(temperatures):
            #going to check if theirs something in pending
            #Else add to pending

            #If would only check once, while will check the current and the others that are left pending.
            while pending and pending[-1][1] < v:
                #This is where I need to calculate how many days it's been
                #Then update my results into results variable.

                #But am I checking current against previous or previous against current?
                    #Previous against current.
                index, temperature = pending.pop()
                diff = i - index
                res[index] = diff


            #I will need the index and value in order to know position and to check temp against another day
            pending.append((i,v))
            
        return res