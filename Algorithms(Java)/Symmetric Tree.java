class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root==null){
            return true;
        }
        return helper(root.left,root.right);
    }
    public boolean helper(TreeNode l,TreeNode r){
        if (l==null || r==null){
            return l==r;
        }
        if (l.val!=r.val){
            return false;
        }
        return helper(l.left,r.right) && helper(l.right,r.left);
    }
}