# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        h=self.height(root)
        ans=[]
        for i in range(h,0,-1):
            arr=[]
            ans.append(self.currentlevel(root,i,arr))
        return ans
    def currentlevel(self,root,level,arr):
        if root==None:
            return
        if level==1:
            arr.append(root.val)
        else:
            self.currentlevel(root.left,level-1,arr)
            self.currentlevel(root.right,level-1,arr)
        return arr
    def height(self,root):
        if root==None:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        if l>r:
            return l+1
        return r+1