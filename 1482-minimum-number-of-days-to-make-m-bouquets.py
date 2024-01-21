from typing import List
from itertools import groupby


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def f(openList):
            li = [sum(1 for _ in group) for key, group in groupby(openList) if key]
            return sum(i // k for i in li)

        l = min(bloomDay) - 1
        r = max(bloomDay) + 1
        while l + 1 != r:
            mid = l + (r - l) // 2
            if f([i <= mid for i in bloomDay]) < m:
                l = mid
            else:
                r = mid

        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDays([1, 10, 3, 10, 2], 3, 1))
    print(solution.minDays([1, 10, 3, 10, 2], 3, 2))
    print(solution.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
    print(solution.minDays([1000000000, 1000000000], 1, 1))
    print(solution.minDays([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2))
