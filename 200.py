import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        
        
        nRow, nCol = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dR, dC in directions:
                    if row + dR in range(nRow) and col + dC in range(nCol) and grid[row + dR][col + dC] == "1" and (row + dR,col + dC) not in visited:
                        visited.add((row + dR,col + dC))
                        q.append((row + dR,col + dC))


        

        for row in range(nRow):
            for col in range(nCol):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands

