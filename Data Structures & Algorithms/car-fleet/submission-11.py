class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        #Need to reorganize so that we can consider cars that are closer to target
        pairs.sort(reverse=True) #We want bigger values, cars that are closer to target at front.
        fleet = [] #Tracking number of fleets

        for p, s in pairs:
            time = (target-p)/s
            fleet.append(time)

            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        
        return len(fleet)