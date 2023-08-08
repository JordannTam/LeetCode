from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op == "*":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                result = val1 * val2
                stack.append(result)
            elif op == "/":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                result = val2 / val1
                stack.append(result)

            elif op == "+":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                result = val1 + val2
                stack.append(result)

            elif op == "-":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                result = val2 - val1
                stack.append(result)
            else:
                stack.append(op)
        return int(stack.pop())



if __name__ == "__main__":
    s = Solution()
    print(Solution.evalRPN(s, ["4","13","5","/","+"]))
    print(Solution.evalRPN(s, ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(Solution.evalRPN(s, ["18"]))
