from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # answer: nums[i - 1] > nums[i]
        # [3,6,7,11]
        # [11, 3, 6, 7]
        # [6, 7, 11, 3]
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        if len(nums) == 1:
            return nums[0]
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1




if __name__ == "__main__":
    s = Solution()
    print(Solution.findMin(s, [3,4,5,1,2]))
    print(Solution.findMin(s, [6,7,0,1,2,4,5]))
    print(Solution.findMin(s, [5,1,2,3,4]))
