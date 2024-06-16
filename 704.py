from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        def binarySearch(l, r):
            if l > r:
                return -1
            mid = l + ((r - l) // 2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(l, mid - 1)
            else:
                return binarySearch(mid + 1, r)
        return binarySearch(left, right)