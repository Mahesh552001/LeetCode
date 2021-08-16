# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res=0
        if root==None:
            return 0
        if root.left and root.left.left==None and root.left.right==None:
            res+=root.left.val
        else:
            res+=self.sumOfLeftLeaves(root.left)
        res+=self.sumOfLeftLeaves(root.right)
        return res