from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        dicts = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }

        stack = []

        for i in s:
            if i not in dicts:
                if stack != [] and i == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(dicts[i])
        if stack == []:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(Solution.isValid(s,"()[]{}"))
