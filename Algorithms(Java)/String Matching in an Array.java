class Solution {
    public List<String> stringMatching(String[] words) {
        List<String> ans=new ArrayList<>();
        HashSet<String> set=new HashSet<>();
        for(int i=0;i<words.length;i++){
            String word=words[i];
            for(int j=0;j<words.length;j++){
                int l=word.length();
                if(j==i || words[j].length()<l){
                    continue;
                }else{
                    for(int k=0;k<(words[j].length()-l+1);k++){
                        if (words[j].substring(k,k+l).equals(word)){
                            if (!set.contains(word)){
                                ans.add(word);
                            }
                            set.add(word);
                            break;
                        }
                    }
                }
            }
        }
        return ans;
    }
}