from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            a = (i, temp)
            while (stack != [] and stack[-1][1] < temp):
                curr = stack.pop()
                res[curr[0]] = i - curr[0]
            stack.append(a)
        return res



            


if __name__ == "__main__":
    s = Solution()
    print(Solution.dailyTemperatures(s, [73,74,75,71,69,72,76,73]))
