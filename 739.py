from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) <= 1:
            return temperatures
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for index, temp in enumerate(temperatures):
            while(stack and temperatures[stack[-1]] < temp):
                i = stack.pop()
                result[i] = index - i
            stack.append(index)
        return result

if __name__ == "__main__":
    s = Solution()
    print(Solution.dailyTemperatures(s, [73,74,75,71,69,72,76,73]))
