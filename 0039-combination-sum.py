from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


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