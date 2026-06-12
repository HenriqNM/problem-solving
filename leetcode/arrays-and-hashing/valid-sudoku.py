from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    row_key = ("row", row, val)
                    col_key = ("col", col, val)
                    grid_key = ("grid", row // 3, col // 3, val)

                    if row_key in seen or col_key in seen or grid_key in seen:
                        return False
                    else:
                        seen.add(row_key)
                        seen.add(col_key)
                        seen.add(grid_key)
        return True