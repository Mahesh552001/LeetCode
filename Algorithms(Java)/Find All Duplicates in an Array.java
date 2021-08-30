class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        HashSet<Integer> h=new HashSet<Integer>();
        List<Integer> l=new ArrayList<Integer>();
        for (int i=0;i<nums.length;i++){
            if (h.contains(nums[i])){
                l.add(nums[i]);
            }
            h.add(nums[i]);
        }
        return l;
    }
}