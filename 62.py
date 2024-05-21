class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 and n < 1:
            return 0
        if m <= 1 and n <= 1:
            return 1
        
        dp = []
        for i in range(m):
            ls = []
            for j in range(n):
                if i == 0:
                    ls.append(1)
                elif j == 0:
                    ls.append(1)
                else:
                    ls.append(0)
            dp.append(ls)
        dp[0][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j - 1]


        for x in dp:
            print(x)
        return dp[m - 1][n - 1]

        
if __name__ == "__main__":
    s = Solution()
    print(Solution.uniquePaths(s, 3, 7))
