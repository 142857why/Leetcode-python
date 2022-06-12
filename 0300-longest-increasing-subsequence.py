import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tail = [0 for _ in range(n)]  # 记录长度为i + 1的LIS最小能放多少（贪心）
        piles = 0  # 当前的最大长度
        maxLen = [0 for _ in range(n)]  # 记录当前index为结尾可以到达的最大长度
        for i in range(n):
            poker = nums[i]
            idx = bisect.bisect_left(tail, poker, lo=0, hi=piles)
            if idx == piles:
                piles += 1
            tail[idx] = poker
            if idx + 1 > maxLen[i]:
                maxLen[i] = idx + 1
        # print(nums)
        # print(maxLen)
        # print(tail)
        # res, i, j = [0 for _ in range(piles)], n - 1, piles
        # while j > 0:
        #     if maxLen[i] == j:
        #         j -= 1
        #         res[j] = nums[i]
        #     i -= 1
        # print(res)
        return piles


if __name__ == '__main__':
    a = [7, 7, 7, 7, 7, 7, 7, 7]
    # a = [1, 2, 8, 6, 4]
    sol = Solution()
    print(sol.lengthOfLIS(a))

