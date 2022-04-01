from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rankings = [[i, sum(troop)] for i, troop in enumerate(mat)]
        rankings.sort(key=lambda x:x[1])
        ans = [rankings[i][0] for i in range(k)]
        return ans


if __name__ == '__main__':
    sol = Solution()
    mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
    k = 3
    print(sol.kWeakestRows(mat, k))