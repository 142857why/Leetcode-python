from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                prefix_sum += nums[i]
            else:
                break
        # print(prefix_sum)

        while prefix_sum in nums:
            prefix_sum += 1

        return prefix_sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingInteger([1, 2, 3, 2, 5]))
    print(sol.missingInteger([3,4,5,1,12,14,13]))
