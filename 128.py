from typing import List


class Solution:
    # My attempt:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     result = {}
    #     snums = set(nums)
    #     for num in snums:
    #         result[str(num)] = set(str(num))

    #     for num in snums:
    #         if str(num + 1) in result:
    #             result[str(num + 1)].update(result[str(num)])
    #         if str(num - 1) in result:
    #             result[str(num - 1)].update(result[str(num)])

    #     longest = 0
    #     for _, v in result.items():
    #         n = len(v)
    #         if n > longest:
    #             longest = n

    #     print(result)
    #     return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        setNums = set(nums)

        for num in setNums:
            if num - 1 not in setNums:
                length = 1
                while num + length in setNums:
                    length += 1
                if length > longest:
                    longest = length
        return longest


if __name__ == "__main__":
    s = Solution()
    print(Solution.longestConsecutive(s, [100, 4, 200, 1, 3, 2]))
