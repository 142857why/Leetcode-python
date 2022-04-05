from collections import deque
from typing import List
from TreeHelper.binary_tree import *

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        stack, res = [root], deque()
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])

            elif isinstance(i, int):
                if len(res) < k:
                    res.append(i)
                else:
                    if abs(res[0] - target) > abs(i - target):
                        res.append(i)
                        res.popleft()

        return list(res)


if __name__ == '__main__':
    s = "[4, 2, 5, 1, 3]"
    root = stringToTreeNode(s)
    t = 3.13
    k = 2
    sol = Solution()
    print(sol.closestKValues(root, t, k))