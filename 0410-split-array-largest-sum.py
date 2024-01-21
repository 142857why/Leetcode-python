from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def numOfSplit(maxSum):
            # 用贪心法，每次尽可能多的分组
            numOfSplit = 1
            curSum = 0
            for num in nums:
                if curSum + num > maxSum:
                    numOfSplit += 1
                    curSum = 0

                curSum += num
            return numOfSplit

        # 二分猜答案
        l = max(nums) - 1
        r = sum(nums)
        while l + 1 != r:
            mid = l + (r - l) // 2
            # print("l, r, mid = ", l, r, mid)
            # print('numOfSplit(mid) = ', numOfSplit(mid))
            if numOfSplit(mid) > k:
                l = mid
            else:
                r = mid
        return r


if __name__ == '__main__':
    solution = Solution()
    # print(solution.splitArray([7, 2, 5, 10, 8], 2))
    # print(solution.splitArray([1, 2, 3, 4, 5], 2))
    print(solution.splitArray([1, 4, 4], 3))
