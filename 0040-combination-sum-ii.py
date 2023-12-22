from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates: List[int], target: int, start: int, combination: List[int], results: List[List[int]]):
        if target < 0:
            return
        if target == 0:
            results.append(combination[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i + 1, combination, results)
            combination.pop()


if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(solution.combinationSum2(candidates, target))
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(solution.combinationSum2(candidates, target))
