from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for index, n in enumerate(numbers):
        #     if target - n in numbers:
        #         if target - n == n and numbers.count(n) > 1:
        #             count = 0
        #             for i in range(len(numbers)):
        #                 if numbers[i] == n:
        #                     if count == 1:
        #                         return [index + 1, i + 1]

        #                     count += 1

        #         return [index + 1, numbers.index(target - n) + 1]

        d = {}
        for index, v in enumerate(numbers):
            if v not in d:
                d[v] = []
            d[v].append(index)

        for index, v in enumerate(numbers):
            key = target - v

            if key in d:
                if d[key][0] == index:
                    if len(d[key]) == 1:
                        continue
                    else:
                        return [index + 1, d[key][1] + 1]
                else:
                    return [index + 1, d[key][0] + 1]


if __name__ == "__main__":
    s = Solution()
    print(Solution.twoSum(s, [2, 3, 4], 6))
