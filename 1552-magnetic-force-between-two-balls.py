from typing import List
import bisect


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def f(distance):
            count = 1
            curr = position[0]
            while (idx := bisect.bisect_left(position, curr + distance)) < n:
                curr = position[idx]
                count += 1
            print('distance = ' + str(distance) + ', count = ' + str(count))
            return count


        l = float('inf')
        for i in range(1, n):
            l = min(l, position[i] - position[i - 1])
        l -= 1
        r = position[-1] - position[0] + 1
        while l + 1 != r:
            mid = l + (r - l) // 2
            print('l = ' + str(l) + ', r = ' + str(r) + ', mid = ' + str(mid))
            if f(mid) >= m:
                l = mid
            else:
                r = mid

        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDistance([1, 2, 3, 4, 7], 3))
    print(solution.maxDistance([5, 4, 3, 2, 1, 1000000000], 2))
