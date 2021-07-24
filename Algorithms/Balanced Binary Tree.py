class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        lh=self.height(root.left) 
        rh=self.height(root.right)
        if abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
        
    def height(self,root):
        if root==None:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        if l>r:
            return l+1
        return r+1