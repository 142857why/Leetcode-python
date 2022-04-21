from typing import List
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # 建图
        g = [[] for _ in range(n)] # 邻接list的方式

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        parents = [0] * n

        # BFS, parents 用于记录路径
        def bfs(start: int):
            global v
            vis = [False] * n
            vis[start] = True

            q = deque([start])
            while q:
                v = q.popleft()
                for w in g[v]:
                    if not vis[w]:
                        vis[w] = True
                        parents[w] = v  # 记录路径
                        q.append(w)

            return v

        # 找出从0的最远点x，然后找距离节点x最远的节点y，然后找到节点y与节点x的路径；x ---> y中间的就是根节点
        x = bfs(0)
        y = bfs(x)

        # 利用parents的信息，反向找回x
        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]

        m = len(path)
        # 如果m是偶数，根节点可以是中间两个
        # 如果m是奇数，那根节点就是中间那个
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(sol.findMinHeightTrees(n, edges))