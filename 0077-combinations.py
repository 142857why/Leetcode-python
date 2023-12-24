from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        self.dfs(n, k, 1, [], results)
        return results

    def dfs(self, n: int, k: int, start: int, combination: List[int], results: List[List[int]]):
        if k == 0:
            results.append(combination[:])
            return

        for i in range(start, n + 1):
            combination.append(i)
            # k - 1 because we have added one element to the combination
            # i + 1 because we cannot reuse the same element
            self.dfs(n, k - 1, i + 1, combination, results)
            combination.pop()


if __name__ == '__main__':
    solution = Solution()
    n = 4
    k = 2
    print(solution.combine(n, k))
    n = 1
    k = 1
    print(solution.combine(n, k))