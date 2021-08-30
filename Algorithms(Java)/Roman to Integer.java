class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> m = new HashMap<Character,Integer>();
        m.put('I', 1);
        m.put('V', 5);
        m.put('X', 10);
        m.put('L', 50);
        m.put('C', 100);
        m.put('D', 500);
        m.put('M', 1000);
        int n=s.length();
        int ans=m.get(s.charAt(n-1));
        for(int i=n-2;i>=0;i--){
            int curr=m.get(s.charAt(i));
            int next=m.get(s.charAt(i+1));
            ans+=curr<next?-curr:curr;
        }
        return ans;
    }
}


//or


class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> m = new HashMap<Character,Integer>();
        m.put('I', 1);
        m.put('V', 5);
        m.put('X', 10);
        m.put('L', 50);
        m.put('C', 100);
        m.put('D', 500);
        m.put('M', 1000);
        int n=s.length();
        int ans=m.get(s.charAt(n-1));
        for(int i=n-1;i>0;i--){
            int curr=m.get(s.charAt(i));
            int prev=m.get(s.charAt(i-1));
            ans+=curr>prev?-prev:prev;
        }
        return ans;
    }
}
