from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            d[str(num)] = index

        for index, num in enumerate(nums):
            if str(target - num) in d:
                if d[str(target - num)] == index:
                    continue
                return [index, d[str(target - num)]]

        return [0, 0]


if __name__ == "__main__":
    s = Solution()
    print(Solution.twoSum(s, [2, 3, 4], 6))
