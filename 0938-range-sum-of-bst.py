from TreeHelper.binary_tree import *


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        stack, res = [root], 0
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                if low < i.val < high:
                    stack.extend([i.right, i.val, i.left])
                elif i.val < low:
                    stack.extend([i.right])
                elif i.val == low:
                    stack.extend([i.right, i.val])
                elif i.val > high:
                    stack.extend([i.left])
                elif i.val == high:
                    stack.extend([i.val, i.left])
            elif isinstance(i, int):
                res += i

        return res


if __name__ == '__main__':
    root_string = "[10,5,15,3,7,13,18,1,null,6]"
    root = stringToTreeNode(root_string)
    sol = Solution()
    low, high = 6, 10
    print(sol.rangeSumBST(root, 6, 10))