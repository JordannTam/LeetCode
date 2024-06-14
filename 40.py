from collections import Counter
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        solution = []
        n = len(candidates)
        nums = sorted(candidates)
        print("nums: ", nums)

        def backtrack(start, remain):
            if remain == 0:
                result.append(solution[:])
                return
            if remain < 0:
                return
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]: 
                    print("result: ",result,", solution: ", solution, ", nums[i]: ", nums[i], ", i: ", i, ", start: ", start, ", remain: ", remain)
                    continue
                solution.append(nums[i])
                backtrack(i + 1, remain - nums[i])
                solution.pop()
        backtrack(0, target)
        return result


if __name__ == "__main__":
    s = Solution()
    print(Solution.combinationSum2(s, [2,5,2,1,2], 5))