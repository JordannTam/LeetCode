from collections import defaultdict
from typing import List


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     result = [[strs[0]]]
    #     if len(strs) <= 1:
    #         return result
    #     for s in strs[1:]:
    #         hasAnagrams = False
    #         for a in result:
    #             if len(a[0]) != len(s):
    #                 continue
    #             hasDiff = False
    #             for c in set(a[0]):
    #                 if a[0].count(c) != s.count(c):
    #                     hasDiff = True
    #                     break
    #             if hasDiff:
    #                 continue
    #             else:
    #                 a.append(s)
    #                 hasAnagrams = True
    #                 break
    #         if not hasAnagrams:
    #             result.append([s])
    #     return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            d["".join(sorted(word))].append(word)
        return list(d.values())
