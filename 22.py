from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, string):
            curr = string
            if left == n and right == n:
                result.append(string)
                return
            if right > left or left > n:
                return
            
            curr += "("
            backtrack(left + 1, right, curr)
            curr = curr[:-1]

            curr += ")"
            backtrack(left, right + 1, curr)
            curr = curr[:-1]

        backtrack(0, 0, "")
        return result


if __name__ == "__main__":
    s = Solution()
    print(Solution.generateParenthesis(s, 3))
