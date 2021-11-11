class Solution {
    TreeNode ans=new TreeNode();
    public final TreeNode getTargetCopy(final TreeNode o, final TreeNode c, final TreeNode t) {
        if (o==null || c==null){
            return null;
        }
        if (o==t){
            ans=c;
        }
        getTargetCopy(o.left,c.left,t);
        getTargetCopy(o.right,c.right,t);
        return ans;
    }
}