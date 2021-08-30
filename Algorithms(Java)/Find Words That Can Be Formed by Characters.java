class Solution {
    public int countCharacters(String[] words, String chars) {
        int count=0;
        HashMap<Character,Integer> h=new HashMap<Character,Integer>();
        for(int i=0;i<chars.length();i++){
            h.put(chars.charAt(i),h.getOrDefault(chars.charAt(i),0)+1);
        }
        for (int i=0;i<words.length;i++){
            HashMap<Character,Integer> m=new HashMap<Character,Integer>(h);
            String word=words[i];
            int len=word.length();
            int c=0;
            for (int j=0;j<word.length();j++){
                if (m.containsKey(word.charAt(j))){
                    if (m.get(word.charAt(j))>0){
                        c++;
                        m.put(word.charAt(j),m.get(word.charAt(j))-1);
                    }
                    else
                        break;
                }else 
                    break;
            }
            if (c==len){
                count+=len;
            }
        }
        return count;
    }
}