from TreeHelper.binary_tree import *
from typing import Optional, List

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = list()

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return

            nodes.append((col, row, node.val))
            # col是排序的第一关键字，row是第二关键字，val是第三关键字
            dfs(node.left, row + 1, col - 1)
            dfs(node.right,row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()

        ans, lastCol = list(), float('-inf')
        for col, row, value in nodes:
            if col != lastCol:
                lastCol = col
                ans.append(list())
                
            ans[-1].append(value)

        return ans


if __name__ == '__main__':
    s = "[1,2,3,4,6,5,7]"
    root = stringToTreeNode(s)

    sol = Solution()
    print(sol.verticalTraversal(root))
