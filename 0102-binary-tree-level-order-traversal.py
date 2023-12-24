import collections
from typing import List, Optional

from TreeHelper.binary_tree import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []
        queue = collections.deque([root])
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            results.append(currentLevel)
        return results


if __name__ == '__main__':
    solution = Solution()
    s = '[3,9,20,null,null,15,7]'
    root = stringToTreeNode(s)
    print(solution.levelOrder(root))
