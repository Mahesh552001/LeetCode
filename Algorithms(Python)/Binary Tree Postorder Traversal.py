class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def po(root):
            if root==None:
                return
            po(root.left)
            po(root.right)
            arr.append(root.val)
        arr=[]
        po(root)
        return arr