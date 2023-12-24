class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
import collections

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Find all nodes
        nodes = self.findNodes(node)
        # Clone all nodes
        mapping = self.cloneNodes(nodes)
        # Clone all edges
        self.cloneEdges(nodes, mapping)
        return mapping[node]

    def findNodes(self, node: 'Node') -> list['Node']:
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            currentNode = queue.popleft()
            for neighbor in currentNode.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return list(visited)

    def cloneNodes(self, nodes: list['Node']) -> dict['Node', 'Node']:
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        return mapping

    def cloneEdges(self, nodes: list['Node'], mapping: dict['Node', 'Node']) -> None:
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)


if __name__ == '__main__':
    solution = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)
    print(node1, node1.val, node1.neighbors)
    cloned_node1 = solution.cloneGraph(node1)
    print(cloned_node1, cloned_node1.val, cloned_node1.neighbors)

