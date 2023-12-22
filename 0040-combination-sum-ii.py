from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(solution.combinationSum2(candidates, target))
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(solution.combinationSum2(candidates, target))
