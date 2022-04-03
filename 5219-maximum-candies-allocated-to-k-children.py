from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # candies.sort()
        max_alloc = sum(candies) // k
        if max_alloc == 0:
            return 0

        l, r = 1, max(candies)
        ans = None
        # print(l, r)
        while l <= r:
            m = l + (r - l) // 2

            cnt = 0
            for x in candies:
                cnt += x // m

            if cnt >= k:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans


if __name__ == '__main__':
    '''
    给你一个 下标从 0 开始 的整数数组 candies 。数组中的每个元素表示大小为 candies[i] 的一堆糖果。你可以将每堆糖果分成任意数量的 子堆 ，但 无法 再将两堆合并到一起。

    另给你一个整数 k 。你需要将这些糖果分配给 k 个小孩，使每个小孩分到 相同 数量的糖果。每个小孩可以拿走 至多一堆 糖果，有些糖果可能会不被分配。

    返回每个小孩可以拿走的 最大糖果数目 。
    '''
    sol = Solution()
    candies = [1, 2, 3, 4, 10]
    k = 5
    print(sol.maximumCandies(candies, k))


