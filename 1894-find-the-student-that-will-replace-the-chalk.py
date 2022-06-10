import bisect
from typing import List


def get_prefix_sum(nums):
    prefix_sum = [0]
    for i in range(1, len(nums) + 1):
        prefix_sum.append(prefix_sum[i - 1] + nums[i - 1])

    return prefix_sum


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        ps = get_prefix_sum(chalk)
        print(ps)
        l, r = 0, len(chalk) - 1
        # 转化成了找右侧边界，例如此时ps = [0, 3, 7, 8, 10], k = 5
        # 想找到7的index
        # -1 以后即为原数组答案

        return bisect.bisect_right(ps, k) - 1


if __name__ == '__main__':
    c = [3, 4, 1, 2]
    k = 25
    sol = Solution()
    print(sol.chalkReplacer(c, k))
