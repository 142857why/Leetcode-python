import bisect
from typing import List, Optional
from TreeHelper.binary_tree import *


class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        def in_order(root: Optional[TreeNode]):
            stack, res = [root], []
            while stack:
                i = stack.pop()
                if isinstance(i, TreeNode):
                    stack.extend([i.right, i.val, i.left])
                elif isinstance(i, int):
                    res.append(i)

            return res

        nums = in_order(root)
        # 倒序所有的ops
        ans = 0
        for op in ops[::-1]:
            l = bisect.bisect_left(nums, op[1])
            r = bisect.bisect(nums, op[2]) - 1
            if l > r:
                continue
            if op[0] == 1:
                ans += (r - l + 1)

            # 删除这一次的op
            nums[l:r + 1] = []

        return ans


if __name__ == '__main__':
    root = "[4, 2, 7, 1, null, 5, null, null, null, null, 6]"
    root = stringToTreeNode(root)
    sol = Solution()
    ops = [[0, 2, 2], [1, 1, 5], [0, 4, 5], [1, 5, 7]]
    print(sol.getNumber(root, ops))
