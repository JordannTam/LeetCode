from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:        

        l = 0
        r = len(nums) - 1

        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l]:
                if target >= nums[l] or target < nums[mid]:
                    # [6,7*,0,1,2,4,5] 
                    # [6,7,0*,1,2,4,5]
                    r = mid - 1
                else:
                    # [6,7,0,1,2,4*,5]
                    l = mid + 1
            else:
                if target < nums[l] or target >= nums[mid]:
                    # [2,4,5,6,7,0*,1]
                    l = mid + 1
                else:
                    # [2,4*,5,6,7,0,1]
                    r = mid - 1
        return -1







if __name__ == "__main__":
    s = Solution()
    print(Solution.search(s, [6,7,0,1,2,4,5], 4))
    print(Solution.search(s, [6,7,0,1,2,4,5], 3))
    print(Solution.search(s, [4,5,6,7,0,1,2], 0))

