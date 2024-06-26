from pstats import Stats
from typing import List
from collections import Counter, defaultdict
import sorting


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = {}

    #     for num in nums:
    #         if num not in counter:
    #             counter[num] = 0
    #         counter[num] += 1

    #     a = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    #     res = []
    #     for i in range(k):
    #         res.append(a[i][0])
    #     res = res[::-1]
    #     return res

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     sl = sorting.merge(nums)
    #     currNum = {}
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter()
        for n in nums:
            count[n] += 1
        sortedCount = list(count.items())
        sortedCount.sort(key=lambda x: x[1], reverse=True)
        a = list(map(lambda x: x[0], sortedCount))
        return a[:k]


if __name__ == "__main__":
    s = Solution()
    print(Solution.topKFrequent(s, [1, 2, 1, 3, 1, 3], 2))
