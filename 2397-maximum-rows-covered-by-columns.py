from typing import List
from itertools import combinations

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0]) # m rows, n columns

        if numSelect == n:
            return m

        # 预处理每行1的列集合
        row2cols = [0] * m
        for i in range(m):
            row2cols[i] = sum((matrix[i][j] == 1) << j for j in range(n))

        ans = 0
        for comb in combinations(range(n), numSelect):
            cur = sum(1 << col for col in comb)
            covers = sum(cur & cols == cols for cols in row2cols)
            ans = max(ans, covers)
        return ans


if __name__ == '__main__':
    solution = Solution()
    matrix = [[0,1,0,0,1],[1,0,1,1,0],[1,0,0,0,1],[0,1,1,0,0]]
    print(solution.maximumRows(matrix, 2))
    matrix = [[0,1,0],[1,0,1],[1,0,1],[1,1,0]]
    print(solution.maximumRows(matrix, 2))