'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''


class Solution:
    def rightLeafSum(self,root):
        res=0
        if root==None:
            return res
        if root.right and root.right.left==None and root.right.right==None:
            res+=root.right.data
        else:
            res+=self.rightLeafSum(root.right)
        res+=self.rightLeafSum(root.left)
        return res