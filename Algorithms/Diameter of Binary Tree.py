# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameter(root):
            if root==None:
                return 0
            l=diameter(root.left)
            r=diameter(root.right)
            nonlocal dia
            dia=max(l+r,dia)
            if l>r:
                return l+1
            return r+1
        dia=0
        diameter(root)
        return dia