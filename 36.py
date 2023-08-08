from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i].count(board[i][j]) > 1:
                    return False
                for n in range(9):
                    if i != n and board[n][j] == board[i][j]:
                        return False

                rowArea = int(i / 3)
                colArea = int(j / 3)
                for a in range(3):
                    for b in range(3):
                        if rowArea * 3 + a == i and colArea * 3 + b == j:
                            continue
                        if board[i][j] == board[rowArea * 3 + a][colArea * 3 + b]:
                            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(
        Solution.isValidSudoku(
            s,
            board=[
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        )
    )

    print(
        Solution.isValidSudoku(
            s,
            [
                [".", ".", "4", ".", ".", ".", "6", "3", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                [".", ".", ".", "5", "6", ".", ".", ".", "."],
                ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                [".", ".", ".", "7", ".", ".", ".", ".", "."],
                [".", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ],
        )
    )
