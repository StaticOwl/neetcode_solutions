#point to be noted, it's a binary search tree so left < root < right value wise
#intuition: given bst, if p and q both are less than root, then the root should be in the left, if greater then right
# but if any of them if less and other is greater, that means that root is the value where we can bound.
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', queue=[]) -> 'TreeNode':
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root