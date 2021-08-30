class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length();
        char[] c=s.toCharArray();
        int start=0;
        int result=0;
        HashMap<Character,Integer> h = new HashMap<Character,Integer>();
        for (int i=0;i<n;i++){
            if (h.containsKey(c[i])){
                start=Math.max(start,h.get(c[i])+1);   //abba
            }
            result=Math.max(result,i-start+1);
            h.put(c[i],i);
        }
        return result;
    }
}
