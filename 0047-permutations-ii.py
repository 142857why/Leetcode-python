from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False] * len(nums)
        permutations = []
        self.dfs(nums, visited, [], permutations)
        return permutations

    def dfs(self, nums, visited, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(permutation)
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            # This is the key to avoid duplicates
            # 不同位置上的相同数字，必须按照顺序用
            # If the current number is the same as the previous number,
            # and the previous number is not visited
            # then skip the current number
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            permutation.append(nums[i])

            self.dfs(nums, visited, permutation.copy(), permutations)

            permutation.pop()
            visited[i] = False


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))
    print(solution.permuteUnique([1, 2, 3]))