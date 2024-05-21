from collections import Counter
from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         s = set(nums)
#         return len(nums) != len(s)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter()

        # using a hashmap dictionary
        count = {}
        for num in nums:
            count[num] += 1
        for n in count.values():
            if n > 1:
                return True
        return False
        