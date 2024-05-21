
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)
        
        dp = []

        for _ in range(m + 1):
            ls = []
            for _ in range(n + 1):
                ls.append(0)
            dp.append(ls)
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print(text2.split(", "))
        # for i, x in enumerate(dp):
        #     print(text1[i - 1], x)

        return dp[-1][-1]


        
if __name__ == "__main__":
    s = Solution()
    print(Solution.longestCommonSubsequence(s, "stone", "longest"))
