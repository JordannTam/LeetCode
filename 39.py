from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        result = []
        nums = sorted(candidates)
        n = len(nums)

        def backtrack(k, remain):
            if remain == 0:
                result.append(solution[:])
                return
            if remain < 0:
                return
            for index in range(k, n):
                solution.append(nums[index])
                backtrack(index, remain - nums[index])
                solution.pop()
        backtrack(0, target)
        return result



if __name__ == "__main__":
    s = Solution()
    print(Solution.combinationSum(s, [2,3,5], 8))