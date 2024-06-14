from typing import List
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) < 2:
        #     return False
        # dicts = {
        #     '{' : '}',
        #     '[' : ']',
        #     '(' : ')'
        # }

        # stack = []

        # for i in s:
        #     if i not in dicts:
        #         if stack != [] and i == stack[-1]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(dicts[i])
        # if stack == []:
        #     return True
        # else:
        #     return False

        stack = deque()
        d = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        # end = {
        #     ')': '(',
        #     '}': '{',
        #     ']': '['
        # }

        for ele in s:
            # Come with a end parentheses and start exist before
            if ele not in d and len(stack) == 0:
                return False
            if ele in d:
                stack.append(d[ele])
            else:
                t = stack.pop()
                if ele != t:
                    return False
        # if the loop is ended and still having element in the stack
        if len(stack) != 0:
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(Solution.isValid(s,"([])"))
