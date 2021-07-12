# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root==None:
            return 0
        else:
            s=0
            if root.val<=high and root.val>=low:
                s+=root.val
            s+=self.rangeSumBST(root.left,low,high)
            s+=self.rangeSumBST(root.right,low,high)
            return s
        