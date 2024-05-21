from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix = [1 for _ in nums]
#         suffix = [1 for _ in nums]
#         n = len(nums) - 1
#         result = [1 for _ in nums]
#         for i in range(n + 1):
#             if i != 0:
#                 prefix[i] = prefix[i - 1] * nums[i]
#                 suffix[n - i] = suffix[n - i + 1] * nums[n - i]
#             else:
#                 suffix[n - i] = nums[n - i]
#                 prefix[i] = nums[i]
#         for i in range(n + 1):
#             if i == 0:
#                 result[i] = suffix[i + 1]
#             elif i == n:
#                 result[i] = prefix[i - 1]
#             else:
#                 result[i] = prefix[i - 1] * suffix[i + 1]
#         return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        # [1, 1, 2*1, 3*2]
        # [4, 3, 2, 1]
        # [6, 2, 1, 1]
        # [6 *1, 2 *4, 1* 4*3, 1* 4*3*2]

        prefix = [1 for _ in range(len(nums) + 1)]
        firstRound = self.prefixMul(nums, prefix)[:-1]
        a = list(reversed(firstRound))
        a.append(1)
        print("a: ", a)
        b = list(reversed(nums))
        secondRound = self.prefixMul(b, a)[:-1]
        return list(reversed(secondRound))
    
    def prefixMul(self, nums: List[int], prefix) -> List[int]:
        a = [1 for _ in range(len(nums) + 1)]
        for index, num in enumerate(nums):
            # print("prefix[index]: ", prefix[index], ", num: ", num)
            a[index + 1] = num * a[index]
            prefix[index] = a[index] * prefix[index]
        return prefix


def prefixSum(nums):
    prefix = [0 for _ in range(len(nums))]
    for index, num in enumerate(nums):
        prefix[index] = prefix[index - 1] + num
    return prefix
if __name__ == "__main__":
    s = Solution()
    # assert(Solution.productExceptSelf(s, [1,2,3,4]), [24,12,8,6])
    print(Solution.productExceptSelf(s, [1, 2, 3, 4]))
    # print(prefixSum([1,2,3,4]))
