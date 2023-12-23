from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums: List[int], startIndex: int, subset: List[int], results: List[List[int]]) -> None:
        results.append(subset[:])

        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2]
    print(solution.subsetsWithDup(nums))
    nums = [0]
    print(solution.subsetsWithDup(nums))