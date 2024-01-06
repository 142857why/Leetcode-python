from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxs = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j]) - 1
                    rows[i] |= 1 << n
                    cols[j] |= 1 << n
                    boxs[i // 3 * 3 + j // 3] |= 1 << n

        def is_valid(n, r, c):
            nonlocal rows, cols, boxs
            return not (rows[r] & (1 << n) or cols[c] & (1 << n) or boxs[r // 3 * 3 + c // 3] & (1 << n))

        def dfs(pos: int) -> bool:
            nonlocal rows, cols, boxs
            if pos == 81:
                return True
            row, col = pos // 9, pos % 9
            if board[row][col] != '.':
                return dfs(pos + 1)
            else:
                for i in range(1, 10):
                    if is_valid(i - 1, row, col):
                        rows[row] |= 1 << (i - 1)
                        cols[col] |= 1 << (i - 1)
                        boxs[row // 3 * 3 + col // 3] |= 1 << (i - 1)
                        board[row][col] = str(i)
                        if dfs(pos + 1):
                            return True
                        else:
                            board[row][col] = '.'
                            rows[row] &= ~(1 << (i - 1))
                            cols[col] &= ~(1 << (i - 1))
                            boxs[row // 3 * 3 + col // 3] &= ~(1 << (i - 1))

        dfs(0)


if __name__ == '__main__':
    solver = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solver.solveSudoku(board)
    print(board)
