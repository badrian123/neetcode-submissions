class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #So I need to combine the position and speed into one list as tuples
        #I am going to use a stack but it is going to keep track of car fleet and will be the final result
        #Oh the pair also needs to be sorted but in reverse so that those closer to destination are processed first
        #The math is going to be time = (target - p)/speed
            #The time will determine the fleet
        #Now, we would need to account for cars that are behind because
            #we don't want them to move ahead of the car infront
        
        #Initial Layout Done :)
        pair = [(p, s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            #What do I need to do here?
            stack.append((target - p) / s)

            #Would it be a while or a if?  
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)