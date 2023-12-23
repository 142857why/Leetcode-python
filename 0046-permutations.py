from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.dfs(nums, [], permutations)
        return permutations

    def dfs(self, nums: List[int], permutation: List[int], permutations: List[List[int]]) -> None:
        if len(nums) == len(permutation):
            permutations.append(permutation[:])
            return

        for num in nums:
            if num in permutation:
                continue

            permutation.append(num)
            self.dfs(nums, permutation, permutations)
            permutation.pop()


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))
    nums = [0, 1]
    print(solution.permute(nums))
    nums = [1]
    print(solution.permute(nums))
