from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        s = 0
        for num in nums:
            if num % 2 == 0:
                s += 1
        return s >= 2


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print(solution.hasTrailingZeros(nums))
