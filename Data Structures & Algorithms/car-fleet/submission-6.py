class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #Position and speed belong to the same car. -Done
        #All cars are heading to the same target.

        #Rules:
            #a car behind the front car can not pass infront of it
                #It can only catch up & drive at same speed but not pass it.
        #Output
            #return the number of different car Fleets that will arrive at the destination.
            #No duplicates


        #So how would i figure this out?
        #I know that all of the cars are heading to the same destination.
        #I know that I am going to have to iterate through the cars list.
        #I know that I am going to have to keep track of the number of fleets.

        #How am i going to keep track of the number of fleets.
            #So fleets can't be the same or greater than the one in the front of it.
            #So some removal is done.
        
        #Well I will need to determine how much time it will take each car to arrive to it's destination. -Done
        #time = (destination - p) / s -Done 

        #With this time, I can use that info to see if a fleet already exists.
        #Meaning the fleet will be based on time. -Done
        #I am also going to go with the higher value. -Done

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = []

        for p, s in cars:
            time = (target - p)/s
            #so how do I determine if I am going to add it to the fleet or not.
            #i think right off the bat it is added.
            fleets.append(time)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
            #while fleets has something and going to check if the value inside of the fleet is greater than the new value
            #or else, pop the new value out of the fleet.
        
        return len(fleets)


