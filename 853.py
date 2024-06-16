from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # fleet = 0
        # curr = []
        # n = len(position)
        # fleetList = [1] * n
        # mask = [0] * n

        # for i in range(n):
        #     curr.append(target - position[i])
        # prev = curr[:]

        # while(curr != mask):
        #     print(curr)
        #     for i in range(n):
        #         for j in range(i + 1, n):
        #             if curr[i] >= curr[j] and curr[i] <= prev[j]:
        #                 fleetList[i] = 0
        #                 curr[i] = curr[j]
        #                 speed[i] = speed[j]
        #     for i in range(n):
        #         if curr[i] != 0:
        #             prev[i] = curr[i]
        #             curr[i] = curr[i] - speed[i]
        # for i in range(n):
        #     if fleetList[i] == 1:
        #         fleet += 1
        # print(curr)
        if len(position) <= 1:
            return 1 

        fleet = len(position)
        ps = list(zip(map(lambda x: target - x, position), speed))
        ps = sorted(ps, key=lambda x: x[0])
        stack = []
        roundsToEnd = list(map(lambda x: x[0]/x[1] ,ps))
        for i in range(1, len(roundsToEnd)):
            if roundsToEnd[i] <= roundsToEnd[i - 1]:
                roundsToEnd[i] = roundsToEnd[i - 1]
                fleet -= 1
        
        
        return fleet

if __name__ == "__main__":
    s = Solution()
    # print(Solution.carFleet(s, target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
    print(Solution.carFleet(s, target = 10, position = [6, 8], speed = [3, 2]))
