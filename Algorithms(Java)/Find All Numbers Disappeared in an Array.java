class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n=nums.length;
        int[] arr=new int[n+1];
        for(int i:nums){
            arr[i]++;
        }
        List<Integer> al=new ArrayList<Integer>();
        for(int i=1;i<=n;i++){
            if (arr[i]==0)
                al.add(i);
        }
        return al;
    }
}