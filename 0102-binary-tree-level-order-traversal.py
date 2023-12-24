from typing import List, Optional

from TreeHelper.binary_tree import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    solution = Solution()
    s = '[3,9,20,null,null,15,7]'
    root = stringToTreeNode(s)
    print(solution.levelOrder(root))
