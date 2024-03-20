#recursive solution 30 ms
def invert(self, root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert(root.left)
        self.invert(root.right)
        
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    self.invert(root)
    return root