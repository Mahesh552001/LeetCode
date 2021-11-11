class Solution {
    public String reverseStr(String s, int k) {
        StringBuilder sb=new StringBuilder(s);
        for(int i=0;i<s.length();i+=2*k){
            int m=i,n=Math.min(i+k-1,s.length()-1);
            while(m<n){
                char temp=sb.charAt(m);
                sb.setCharAt(m,sb.charAt(n));
                sb.setCharAt(n,temp);m++;n--;
            }
        }
        return sb.toString();
    }
}