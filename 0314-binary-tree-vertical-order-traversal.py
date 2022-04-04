from collections import deque
from typing import Optional, List
from TreeHelper.binary_tree import *

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([])
        leftMost, rightMost = 0, 0



if __name__ == '__main__':
    s = "[3,9,20,null,null,15,7]"
    root = stringToTreeNode(s)

    sol = Solution()
    print(sol.verticalOrder(root))
