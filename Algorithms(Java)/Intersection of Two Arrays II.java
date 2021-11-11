class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int n1=nums1.length,n2=nums2.length;
        int i=0,j=0;
        ArrayList<Integer> l=new ArrayList<>();
        while(i<n1 && j<n2){
            if (nums1[i]==nums2[j]){
                l.add(nums1[i]);
                i++;j++;
            }else if(nums1[i]<nums2[j]){
                i++;
            }else{
                j++;
            }
        }
        int[] ans=new int[l.size()];
        for(int k=0;k<l.size();k++)
        {
            ans[k]=l.get(k);
        }   
        return ans;    
    }
}