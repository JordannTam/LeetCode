from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # d = {}
        # result = []
        # storedRes = []
        # setNums = set(nums)

        # for index, num in enumerate(setNums):
        #     if str(num) not in d:
        #         d[str(num)] = []
        #     d[str(num)].append(index)

        # for i, num in enumerate(setNums):
        #     for j, jNum in enumerate(setNums[i + 1 :]):
        #         target = 0 - (num + jNum)
        #         if str(target) in d:
        #             for k in d[str(target)]:
        #                 if k != i and k != j:
        #                     indexRes = sorted([i, j, k])
        #                     res = sorted([num, jNum, target])
        #                     if indexRes not in storedRes and res not in result:
        #                         storedRes.append(indexRes)
        #                         result.append(res)
        # return sorted(result)

        # if num != target and nums[j] != target and d[str(target)] > 1:
        #     res = sorted([num, nums[j], target])
        #     if res not in result:
        #         result.append(res)
        #         d[str(num)] -= 1
        #         d[str(nums[j])] -= 1
        #         d[str(target)] -= 1

        # elif num == target or nums[j] == target:
        #     if num == target and nums[j] == target and d[str(target)] > 2:
        #         res = sorted([num, nums[j], target])
        #         if res not in result:
        #             result.append(res)
        #             d[str(num)] -= 1
        #             d[str(nums[j])] -= 1
        #             d[str(target)] -= 1
        #     if (num != target or nums[j] != target) and d[str(target)] > 1:
        #         res = sorted([num, nums[j], target])
        #         if res not in result:
        #             result.append(res)
        #             d[str(num)] -= 1
        #             d[str(nums[j])] -= 1
        #             d[str(target)] -= 1

        #        else:
        #            continue


        d = {}
        result = set()
        n = len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                target = 0 - (nums[i] + nums[j])
                if target not in d:
                    d[target] = []
                pair = tuple(sorted((i, j)))
                m = list(map(lambda a: (a[0][0], a[1][0]) ,d[target]))
                if pair not in m and pair[0] != pair[1]:
                    d[target].append([(i, nums[i]), (j, nums[j])])

        for index, num in enumerate(nums):
            if num in d:
                for i in d[num]:
                    if i[0][0] != index and i[1][0] != index:
                        ans = [i[0][1], i[1][1], num]
                        a = sorted(ans)
                        result.add(tuple(a))
        result = sorted(result, key=lambda a: a)
        return result




if __name__ == "__main__":
    s = Solution()
    print(Solution.threeSum(s, [-1,0,1,2,-1,-4,-2,-3,3,0,4]))
