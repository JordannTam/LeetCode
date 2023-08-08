# My first approach with DP

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0
#         longList = [[0 for _ in range(len(s))] for _ in range(len(s))]

#         # longList[0].append(1)

#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if s[j] in list(s[i:j]):
#                     longList[i][j] = 1
#                 else:
#                     longList[i][j] = longList[i][j - 1] + 1
#                 # print(f"s[i:j]={s[i:j]} i={i} j={j}")

#         for i in longList:
#             if max(i) > longest:
#                 longest = max(i)
#         return longest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            currList = []
            for j in range(i, len(s)):
                if s[j] not in currList:
                    currList.append(s[j])
                    if n > longest:
                        longest = n

                else:
                    n = len(currList)
                    if n > longest:
                        longest = n
                    break
        return longest


if __name__ == "__main__":
    s = Solution()
    print(Solution.lengthOfLongestSubstring(s, "abcabcbbb"))
