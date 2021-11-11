class Solution {
    
    public List<List<Integer>> levelOrder(TreeNode root) {
        int h=height(root);
        List<List<Integer>> ans=new ArrayList<>();
        for (int i=1;i<=h;i++){
            List<Integer> temp=new ArrayList<>();
            ans.add(currentLevel(root,temp,i));
        }
        return ans;
    }
    public List<Integer> currentLevel(TreeNode root,List<Integer> temp,int level){
        if (root==null){
            return temp;
        }
        if (level==1){
            temp.add(root.val);
        }else{
            currentLevel(root.left,temp,level-1);
            currentLevel(root.right,temp,level-1);
        }
        return temp;
        
    }
    public int height(TreeNode root){
        if (root==null){
            return 0;
        }
        int l=height(root.left);
        int r=height(root.right);
        return Math.max(l,r)+1;
    }
}