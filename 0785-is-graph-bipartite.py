from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)  # number of vertices
        visited = [False] * V
        colors = [-1] * V

        for i in range(V):
            if not visited[i]:
                if not self.dfs(graph, i, visited, colors):
                    return False
        return True

    def dfs(self, graph: List[List[int]], vertex: int, visited: List[bool], colors: List[int]) -> bool:
        visited[vertex] = True

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                colors[neighbor] = 1 - colors[vertex]
                if not self.dfs(graph, neighbor, visited, colors):
                    return False
            elif colors[neighbor] == colors[vertex]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(solution.isBipartite(graph))
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(solution.isBipartite(graph))
    graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [1, 3, 6, 9], [1, 5, 7, 8, 9], [3, 6, 9],
             [2, 3, 4, 6, 9],
             [2, 4, 5, 6, 7, 8]]
    print(solution.isBipartite(graph))
