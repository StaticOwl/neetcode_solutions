#https://www.youtube.com/watch?v=bkxqA8Rfv04
#TODO: Do it again

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], dia=0) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)
            
        dfs(root)
        return res[0]