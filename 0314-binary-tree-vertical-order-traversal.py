from collections import deque
from typing import Optional, List
from TreeHelper.binary_tree import *

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root, 0, 0))
        ans = deque()
        ans.append([])
        leftMost, rightMost = 0, 0
        while q:
            currNode, currX, currY = q.popleft()

            # needs to update ans
            if currY < leftMost:
                ans.appendleft([currNode.val])
                leftMost = currY
            elif currY > rightMost:
                # 比如现在最右index, 即rightMost = 1, 来的currY = 2
                ans.append([currNode.val])
                rightMost = currY
            else:
                # 比如现在最左index, 即leftMost = -1, 来的currY = 1, 那就修改ans[2], 其中2 = currY - leftMost
                ans[currY - leftMost].append(currNode.val)

            if currNode.left:
                q.append((currNode.left, currX + 1, currY - 1))

            if currNode.right:
                q.append((currNode.right, currX + 1, currY + 1))

        return list(ans)


if __name__ == '__main__':
    s = "[3,9,20,null,null,15,7]"
    root = stringToTreeNode(s)

    sol = Solution()
    print(sol.verticalOrder(root))
