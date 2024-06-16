from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while(left <= right):
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                if target in matrix[mid]:
                    return True
                else:
                    return False
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False




if __name__ == "__main__":
    s = Solution()
    print(Solution.searchMatrix(s, matrix = [[1]], target = 2))
    print(Solution.searchMatrix(s, matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
