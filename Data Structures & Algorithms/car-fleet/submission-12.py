class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #I need to combine two list together
        #I need to sort the list based on who is closest to destination.
        #I am going to use a stack in order to keep track of fleets

        #I am using something from the stack in order to determine something.
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        #Now i have a pair of cars sorted in reverse order.
        #I need to look at the time it takes to get to destination.
        #(destination - position)/ speed
        #How am i going to go about this?

        #Oh so iterate through all of the pairs.
        #Then have a way to check if fleet is already in stack.
        #So that's probably what the stack is for.
        
        for p, s in pairs:
            time = (target - p)/ s

            #what am i adding to the stack?
            stack.append(time)

            #Now, I need to determine if I have to add it to the stack or not.
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() 

        return len(stack)
