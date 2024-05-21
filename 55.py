
from typing import List
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        count = len(nums)
        maxNum = nums[0]

        for i, num in enumerate(nums):
            if maxNum < i :
                return False
            if (i + num) > maxNum:
                maxNum = i + num
        if maxNum >= maxNum:
            return True
        else:
            return False
            


if __name__ == "__main__":
    s = Solution()
    print(Solution.canJump(s, [3,2,1,0,4]))
