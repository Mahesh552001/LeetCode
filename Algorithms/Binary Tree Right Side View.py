# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def r(root,level):
            if root==None:
                return
            if level not in dic:
                dic[level]=None
                result.append(root.val)
            r(root.right,level+1)
            r(root.left,level+1)
        dic={}
        result=[]
        r(root,1)
        return result