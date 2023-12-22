from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates: List[int], target: int, start: int, combination: List[int], results: List[List[int]]) -> None:
        if target < 0:
            return
        if target == 0:
            results.append(combination[:])
            return

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            combination.pop()


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(solution.combinationSum(candidates, target))
    candidates = [2, 3, 5]
    target = 8
    print(solution.combinationSum(candidates, target))
    candidates = [2]
    target = 1
    print(solution.combinationSum(candidates, target))
    candidates = [1]
    target = 1
    print(solution.combinationSum(candidates, target))
    candidates = [1]
    target = 2
    print(solution.combinationSum(candidates, target))