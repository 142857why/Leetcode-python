from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        # 把数组与x的差值映射到二维平面上，其实是找底部最低的k个数（左边界）
        # 那初识的时候边界就从len(arr) - k开始 [l, r)

        while l < r:
            m = l + (r - l) // 2
            if (x - arr[m]) > (arr[m + k] - x):
                # 更新条件就是左侧的candidate 和 我们假想的底部m 差距过大，导致右侧"高度"过"高"
                l = m + 1
            else:
                r = m

        return arr[l:l+k]


if __name__ == '__main__':
    sol = Solution()
    a, k, x = [1, 2, 3, 4, 5], 4, -1
    print(sol.findClosestElements(a, k, x))