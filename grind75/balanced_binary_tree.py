# Solution consists of double recursion, one is to find the height of left and right subtrees, another to find the difference in each node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        else:
            leftHeight = self.height(root.left)
            rightHeight = self.height(root.right)
            return max(leftHeight, rightHeight) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        leftHeight = 0
        rightHeight = 0
        if root:
            print(root.val)
            if root.left:
                leftHeight = self.height(root.left)
            if root.right:
                rightHeight = self.height(root.right)
            
            print(leftHeight)
            print(rightHeight)
        
            if abs(leftHeight - rightHeight) <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False
        return True