from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        result = []
        def backtrack():
            if len(solution) == len(nums):
                result.append(solution[:])
                return
            for num in nums:
                if num not in solution:
                    solution.append(num)
                    backtrack()
                    solution.pop()
        backtrack()
        return result


if __name__ == "__main__":
    s = Solution()
    print(Solution.permute(s, [1,2,3]))