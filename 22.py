from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, solution):
            if left == right and left == n:
                result.append(solution)
                return
            if right > left:
                return
            
            if left <= n and right <= n:
                solution += "("
                left += 1
                backtrack(left, right, solution)
                left -= 1
                solution = solution[:-1]

                solution += ")"
                right += 1
                backtrack(left, right, solution)
                right -= 1
                solution = solution[:-1]
        backtrack(0, 0, "")
        return result


    

if __name__ == "__main__":
    s = Solution()
    print(Solution.generateParenthesis(s, 3))
