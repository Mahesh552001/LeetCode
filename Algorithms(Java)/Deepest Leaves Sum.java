/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum,h;
    public int deepestLeavesSum(TreeNode root) {
        h=maxDepth(root);
        return deepSum(root,1);
    }
    public int maxDepth(TreeNode root){
        if (root==null){
            return 0;
        }
        int l=maxDepth(root.left);
        int r=maxDepth(root.right);
        return Math.max(l,r)+1;
    }
    public int deepSum(TreeNode root,int level){
        if (root==null){
            return sum;
        }
        if (level==h){
            sum+=root.val;
        }else{
            deepSum(root.left,level+1);
            deepSum(root.right,level+1);
        }
        return sum;
    }
}