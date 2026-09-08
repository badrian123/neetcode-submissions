class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort(reverse=True)
        fleet = []

        for p,s in cars:
            time = (target-p)/s
            fleet.append(time)
            while len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        
        return len(fleet)