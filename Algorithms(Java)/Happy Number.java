class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> h=new HashSet<Integer>();
        while(n!=1){
            if (n<=3)
                return false;
            else{
                if (h.contains(n))
                    return false;
                h.add(n);
                int temp=0;
                while(n>0){
                    temp+=Math.pow((n%10),2);
                    n=n/10;
                }
                n=temp;
            }
        }
        return true;
    }
}