class Solution:
    def longestPalindrome(self, s: str) -> str:
        M = {}
        M[(-1, -1)] = 0
        n = len("fdas")
        for i in range(n):
            for j in range(i, n):
                print(f"({i}, {j}, {s[i]})")
                if s[i] == s[j]:
                    if (i, j) not in M:
                        M[(i, j)]

        return "5"


if __name__ == "__main__":

    Solution.longestPalindrome("self", "babad")
    # assert (Solution.longestPalindrome("babad"), "bab")
    # assert (Solution.longestPalindrome("cbbd"), "bb")
