class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[]

        for i in range(len(position)):
            car.append((position[i],speed[i]))

        car.sort(key=lambda x:x[0], reverse=True)

        fleet=[]
        for p,s in car:
            time=(target-p)/s

            if fleet and time<=fleet[-1]:
                continue

            fleet.append(time)

        return len(fleet)