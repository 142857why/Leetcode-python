from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first increasing element from the right
        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        # If i is not -1, then we found the first increasing element
        if i >= 0:
            # Find the first element that is greater than nums[i] from the right
            while nums[i] >= nums[k]:
                k -= 1

            # Swap nums[i] and nums[k]
            nums[i], nums[k] = nums[k], nums[i]

        # Reverse the elements from j to the end
        j, k = j, len(nums) - 1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print(nums)
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    print(nums)
    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    print(nums)
    nums = [1]
    solution.nextPermutation(nums)
    print(nums)