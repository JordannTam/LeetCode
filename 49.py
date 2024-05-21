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

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     d = defaultdict(list)

    #     for word in strs:
    #         d["".join(sorted(word))].append(word)
    #     return list(d.values())
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        result = []
        # if the two strings are anagram, the sorted(string) would be the same and unique. If we keep the sorted(string) as the key of hashmap, we can get the list of anagrams
        for s in strs:
            a = "".join(sorted(s))
            if a not in hashMap:
                hashMap[a] = []
            hashMap[a].append(s)
        for ls in hashMap.values():
            result.append(ls)
        return ls

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


