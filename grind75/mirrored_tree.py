# Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def mirror(root):
            if root:
                temp = root.right
                root.right = root.left
                root.left = temp
                mirror(root.left)
                mirror(root.right)
            return root
        
        def isSameTree(p, q):
            if p and q:
                if p.val == q.val:
                    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
                else:
                    return  False
            else:
                if p is None and q is None:
                    return True
                else:
                    return False
        if root:
            return isSameTree(root.left, mirror(root.right))
        else:
            return True


# TODO: Do iterative solution for this

