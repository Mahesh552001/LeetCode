class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        HashSet<List<Integer>> h=new HashSet<>();
        List<List<Integer>> ans=new ArrayList<>();
        ans.add(new ArrayList<>());
        for(int i=0;i<nums.length;i++){
            for(int j=0,size=ans.size();j<size;j++){
                List<Integer> subset=new ArrayList<>(ans.get(j));
                subset.add(nums[i]);
                if (!h.contains(subset)){
                    h.add(subset);
                    ans.add(subset);
                }
            }
        }
        return ans;
    }
}