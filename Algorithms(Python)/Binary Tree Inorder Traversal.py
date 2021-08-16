class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def io(root):
            if root==None:
                return None
            io(root.left)
            arr.append(root.val)
            io(root.right)
        arr=[]
        io(root)
        return arr