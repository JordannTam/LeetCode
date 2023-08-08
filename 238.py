from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in nums]
        suffix = [1 for _ in nums]
        n = len(nums) - 1
        result = [1 for _ in nums]
        for i in range(n + 1):
            if i != 0:
                prefix[i] = prefix[i - 1] * nums[i]
                suffix[n - i] = suffix[n - i + 1] * nums[n - i]
            else:
                suffix[n - i] = nums[n - i]
                prefix[i] = nums[i]
        for i in range(n + 1):
            if i == 0:
                result[i] = suffix[i + 1]
            elif i == n:
                result[i] = prefix[i - 1]
            else:
                result[i] = prefix[i - 1] * suffix[i + 1]
        return result


if __name__ == "__main__":
    s = Solution()
    # assert(Solution.productExceptSelf(s, [1,2,3,4]), [24,12,8,6])
    print(Solution.productExceptSelf(s, [1, 2, 3, 4]))
