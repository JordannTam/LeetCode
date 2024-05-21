from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rowCheck(board) and self.columnCheck(board) and self.blockCheck(board)

    def rowCheck(self, board):
        for row in board:
            ls = []
            for element in row:
                if element in ls:
                    return False
                if element != ".":
                    ls.append(element)
        return True
    def columnCheck(self, board):
        for i in range(9):
            ls = []
            for j in range(9):
                if board[j][i] in ls:
                    return False
                if board[j][i] != ".":
                    ls.append(board[j][i])
        return True 
    def blockCheck(self, board):
        # 3 times 
        for h in range(3):
            for k in range(3):
                ls = []
                for i in range(3):
                    for j in range(3):
                        if board[i + (h * 3)][j + (k * 3)] in ls:
                            return False
                        if board[i + (h * 3)][j + (k * 3)] != ".":
                            ls.append(board[i + (h * 3)][j + (k * 3)])
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
