class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #I know this one, we are going to be checking the cars.
        #Will need to sort out the cars based on position b/c some cars are closer to target
        #Also position and speed into one list.

        #(target - position) / speed gives us time.
            #time will be used to determine fleet.
            #However, if there is a car ahead, we can't have the current car be faster or equal
                #Goal is to track as many fleets in these conditions.
        cars = [(p,s) for p,s in zip(position, speed)]
        #Want to process those closer to target first
        cars.sort(reverse=True)
        fleet = []

        for p, s in cars:
            time = (target-p) / s
            fleet.append(time)
            while len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        
        return len(fleet)
