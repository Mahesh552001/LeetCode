class Solution {
    public boolean isValid(String s) {
        HashMap<Character,Character> map=new HashMap<>();
        map.put('(',')');map.put('{','}');map.put('[',']');
        LinkedList<Character> l=new LinkedList<>();
        for(int i=0;i<s.length();i++){
            if (map.containsKey(s.charAt(i))){
                l.add(s.charAt(i));
            }else{
                if(l.isEmpty()){
                   return false; 
                }else if(map.get(l.removeLast())!=s.charAt(i)){
                    return false;
                }
            }
        }
        return l.size()==0?true:false;
    }
}