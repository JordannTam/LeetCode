from typing import List
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         def binarySearchRow(row):
#             mid = len(row) // 2
#             if row[mid] == target:
#                 return True
#             elif len(row) == 1:
#                 return False
#             elif row[mid] > target:
#                 return binarySearchRow(row[:mid])
#             elif row[mid] < target:
#                 return binarySearchRow(row[mid:])
            
#         def binarySearch(column):
#             mid = len(column) // 2
#             if column[mid][0] == target:
#                 return True
#             elif column[mid][0] <= target and column[mid][-1] >= target:
#                 return binarySearchRow(column[mid])
#             elif len(column) == 1:
#                 return False
#             elif column[mid][0] < target:
#                 return binarySearch(column[mid:])
#             elif column[mid][-1] > target:
#                 return binarySearch(column[:mid])
            
#         if len(matrix) == 1:
#             return binarySearchRow(matrix[0])
#         return binarySearch(matrix)




# if __name__ == "__main__":
#     s = Solution()
#     print(Solution.searchMatrix(s, [[1],[3]], 0))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow(left, right):
            if left == right:
                return False

            mid = int((left + right) / 2)
            if target < matrix[mid][0]:
                return findRow(left, mid)
            elif target > matrix[mid][-1]:
                return findRow(mid + 1, right)
            else:
                n = len(matrix[mid])
                return findTarget(matrix[mid], 0, n)

        def findTarget(ls: List[int], left, right) -> bool:
            if left == right:
                return False
            mid = int((left + right) / 2)
            if target < ls[mid]:
                return findTarget(ls, left, mid)
            elif target > ls[mid]:
                return findTarget(ls, mid + 1, right)
            else:
                return True

        n = len(matrix)
        return findRow(0, n)





if __name__ == "__main__":
    s = Solution()
    print(Solution.searchMatrix(s, [[1]], 0))
