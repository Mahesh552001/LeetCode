class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String,Integer> map=new HashMap<String,Integer>();
        for(int i=0;i<list1.length;i++){
            map.put(list1[i],i);
        }
        int minimum=Integer.MAX_VALUE;
        for(int i=0;i<list2.length;i++){
            if (map.containsKey(list2[i])){
                minimum=Math.min(minimum,map.get(list2[i])+i);
                map.put(list2[i],-(map.get(list2[i])+i));
            }
        }
        List<String> l=new ArrayList<String>();
        for(Map.Entry<String,Integer> e:map.entrySet()){
            if (e.getValue()==-minimum){
                l.add(e.getKey());
            }
        }
        return l.toArray(new String[0]);
    }
}