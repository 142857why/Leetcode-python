from typing import List


def count_pairs_distance_leq_than_t(arr: List[int], t: int) -> int:
    l, cnt = 0, 0
    for r in range(len(arr)):
        while arr[r] - arr[l] > t:
            l += 1
        cnt += (r - l)
    return cnt


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 蓝红区间法解题
        l, r = -1, nums[-1] - nums[0] + 1  # 预示着[0, nums[-1] - nums[0]], 答案一定是该区间的整数
        for i in range(r):
            print(count_pairs_distance_leq_than_t(nums, i), end=' ')
        print()
        # l永远表示蓝, r永远表示红
        while l + 1 != r:
            m = (l + r) >> 1
            c = count_pairs_distance_leq_than_t(nums, m)  # 以m为阈值, 有多少数对的距离 <= m
            if c < k:
                l = m
            else:
                r = m
        return r


if __name__ == '__main__':
    a, k = [1, 3, 1, 7, 6, 14, 9], 5  # Expected 2
    sol = Solution()
    print(sol.smallestDistancePair(a, k))
