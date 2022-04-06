from TreeHelper.binary_tree import *

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 利用中序遍历来辅助判断
        stack, last = [root], float('-inf')
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                if i <= last:
                    # 因为要求严格大于和小于
                    return False
                else:
                    last = i

        return True


if __name__ == '__main__':
    s = "[5,1,4,null,null,3,6]"
    root = stringToTreeNode(s)
    # prettyPrintTree(root)
    sol = Solution()
    print(sol.isValidBST(root))