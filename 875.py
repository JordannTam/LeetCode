

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        result = r


        while(l <= r):
            mid = (r + l) // 2
            if mid == 0:
                return result
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total > h:
                l = mid + 1
            else:
                result = min(mid, result)
                r = mid - 1
        return result



if __name__ == "__main__":
    s = Solution()
    print(Solution.minEatingSpeed(s, [3,6,7,11], 8))
    print(Solution.minEatingSpeed(s, [312884470], 968709470))

