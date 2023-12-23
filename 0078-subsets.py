from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums: List[int], startIndex: int, subset: List[int], results: List[List[int]]) -> None:
        results.append(subset[:])

        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))
    nums = [0]
    print(solution.subsets(nums))
