from typing import List
import sys
from collections import Counter

#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        n = len(heights)
        stack = [(0, heights[0])]
        largestArea = 0
        for index, height in enumerate(heights):
            print(largestArea, stack)
            if height > stack[-1][1]:
                stack.append((index, height))
            elif height == stack[-1][1]:
                continue
            else:
                lasti = 0
                while(stack and stack[-1][1] >= height):
                    i, currH = stack.pop()
                    area = currH * (index - i)
                    if area > largestArea:
                        largestArea = area
                    lasti = i
                if not stack or height > stack[-1][1]:
                    stack.append((lasti, height))
                    
        for index, height in stack:
            area = height * (n - index)
            if area > largestArea:
                largestArea = area
        return largestArea




if __name__ == "__main__":
    s = Solution()
    print(Solution.largestRectangleArea(s, [2,1,5,6,2,3]))
