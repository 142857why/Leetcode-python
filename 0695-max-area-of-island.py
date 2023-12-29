from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    ]
    print(solution.maxAreaOfIsland(grid))
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    print(solution.maxAreaOfIsland(grid))
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
    print(solution.maxAreaOfIsland(grid))
    grid = [[1, 1, 1, 1, 1, 1, 1]]
    print(solution.maxAreaOfIsland(grid))
    grid = [[1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1]]
    print(solution.maxAreaOfIsland(grid))