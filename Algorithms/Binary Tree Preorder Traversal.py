class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def po(root):
            if root==None:
                return
            arr.append(root.val)
            po(root.left)
            po(root.right)
        arr=[]
        po(root)
        return arr