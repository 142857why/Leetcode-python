from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        xor_with_k = xor_sum ^ k
        ans = bin(xor_with_k).count('1')

        return ans


if __name__ == '__main__':
    sol =  Solution()
    print(sol.minOperations([2, 1, 3, 4], 1))
    print(sol.minOperations([2, 0, 2, 0], 0))