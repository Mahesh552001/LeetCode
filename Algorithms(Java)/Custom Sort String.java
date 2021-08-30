-+class Solution {
    public String customSortString(String order, String s) {
        HashMap<Character,Integer> map=new HashMap<Character,Integer>();
        for(int i=0;i<s.length();i++){
            map.put(s.charAt(i),map.getOrDefault(s.charAt(i),0)+1);
        }
        String ans="";
        for(int i=0;i<order.length();){
            if (map.containsKey(order.charAt(i))){
                if (map.get(order.charAt(i))==1){
                    ans+=order.charAt(i);
                    map.remove(order.charAt(i));
                }else{
                    ans+=order.charAt(i);
                    map.put(order.charAt(i),map.get(order.charAt(i))-1);
                    continue;
                }
            }
            i++;
        }
        for(Map.Entry entry:map.entrySet()){
            for(int i=0;i<entry.getValue();i++){
                ans+=entry.getKey();
            }
        }
        return ans;
    }
}