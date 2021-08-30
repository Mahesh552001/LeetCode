class Solution {
    public int[] findErrorNums(int[] nums) {
        int n=nums.length;
        int expected=(n*(n+1))/2;
        int actual=0;
        HashSet<Integer> h=new HashSet<Integer>();
        int duplicate=0;
        for (int i:nums){
            if (h.contains(i))
                duplicate=i;
            h.add(i);
            actual+=i;
        }
        return new int[] {duplicate,expected-actual+duplicate};
    }
}