from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        # k is the number of elements in the combination
        # n is the sum of the combination
        self.dfs(k, n, 1, [], results)
        return results

    def dfs(self, k: int, n: int, start: int, combination: List[int], results: List[List[int]]) -> None:
        if k == 0 and n == 0:
            results.append(combination[:])
            return

        for i in range(start, 10):
            combination.append(i)
            # k - 1 because we have added one element to the combination
            # n - i because we have added i to the combination
            # i + 1 because we cannot reuse the same element
            self.dfs(k - 1, n - i, i + 1, combination, results)
            combination.pop()


if __name__ == '__main__':
    solution = Solution()
    k = 3
    n = 7
    print(solution.combinationSum3(k, n))
    k = 3
    n = 9
    print(solution.combinationSum3(k, n))
    k = 4
    n = 1
    print(solution.combinationSum3(k, n))
    k = 3
    n = 2
    print(solution.combinationSum3(k, n))
    k = 9
    n = 45
    print(solution.combinationSum3(k, n))