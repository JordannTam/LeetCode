from typing import List


class Solution:
    # Attempt 1 for all substring

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     substring = {
    #         "value": strs[0],
    #         "position": (0, len(strs[0])),
    #     }
    #     for word in strs[1:]:
    #         wordMaxSubString = {"value": "", "position": (-1, -1)}
    #         wordCurrSub = {"value": "", "position": (-1, -1)}
    #         for i in range(len(word)):
    #             if i >= len(substring["value"]):
    #                 break
    #             if word[substring["position"][0] + i] == substring["value"][i]:
    #                 wordCurrSub["value"] = (
    #                     wordCurrSub["value"] + word[substring["position"][0] + i]
    #                 )
    #                 if wordCurrSub["position"] == (-1, -1):
    #                     wordCurrSub["position"] = (
    #                         substring["position"][0] + i,
    #                         substring["position"][0] + i,
    #                     )
    #                 else:
    #                     wordCurrSub["position"] = (
    #                         wordCurrSub["position"][0],
    #                         substring["position"][0] + i,
    #                     )
    #             else:
    #                 if len(wordCurrSub["value"]) > len(wordMaxSubString["value"]):
    #                     wordMaxSubString = wordCurrSub
    #                 wordCurrSub = {"value": "", "position": (-1, -1)}

    #         if len(wordCurrSub["value"]) > len(wordMaxSubString["value"]):
    #             wordMaxSubString = wordCurrSub

    #         substring = wordMaxSubString

    #     return substring["value"]

    # Attempt 2 with nested loop

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     prefix = strs[0]
    #     for word in strs[1:]:
    #         currPrefix = ""
    #         x = word if len(prefix) > len(word) else prefix
    #         for i in range(len(x)):
    #             print(prefix[i], word[i], i)
    #             if prefix[i] == word[i]:
    #                 currPrefix = currPrefix + word[i]
    #             else:
    #                 prefix = currPrefix
    #                 break
    #         prefix = currPrefix

    #     return prefix

    # Attempt 3 with sorted list

    def longestCommonPrefix(self, strs: List[str]) -> str:
        sl = sorted(strs)
        left = sl[0]
        right = sl[-1]
        n_left = len(left)
        n_right = len(right)
        result = ""

        for i in range(min(n_left, n_right)):
            if left[i] == right[i]:
                result = result + left[i]
            else:
                break
        return result


# def findMatch(strs):
#     re.split("")


if __name__ == "__main__":
    s = Solution()
    print(Solution.longestCommonPrefix(s, ["ab", "a"]))
