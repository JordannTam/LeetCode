import collections
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        result = []
        n = len(nums)
        
        def backtrack(k):
            # if k == n:
            if k == n:
                result.append(solution[:])
                return
            # return
            backtrack(k + 1)
            solution.append(nums[k])
            backtrack(k + 1)
            solution.pop()
        backtrack(0)
        return result

if __name__ == "__main__":
    s = Solution()
    print(Solution.subsets(s, nums = [1,2,3]))
        
