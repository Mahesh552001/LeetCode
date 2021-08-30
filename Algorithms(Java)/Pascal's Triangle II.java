class Solution {
    public List<Integer> getRow(int n) {
        List <Integer> a=new ArrayList<Integer>();
        int i;
        a.add(1);
        for(i=1;i<=n;i++){
            a.add((int)((long)a.get(i-1)*(n-(i-1))/i));
        }   
        return a;
    }
}