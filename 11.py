from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        largest = 0

        while i < j:
            currHeight = height[i] if height[i] < height[j] else height[j]

            v = currHeight * (j - i)
            if v > largest:
                largest = v

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return largest


if __name__ == "__main__":
    s = Solution()
    print(Solution.maxArea(s, [1, 8, 6, 2, 5, 4, 8, 3, 7]))
