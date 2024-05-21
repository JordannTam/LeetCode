from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def recursion (openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                recursion(openN + 1, closeN)
                print("//stack: ", stack)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                recursion(openN, closeN + 1)
                print("//stack: ", stack)
                stack.pop()
        recursion(0, 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(Solution.generateParenthesis(s, 3))
