class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder title=new StringBuilder();
        while(columnNumber!=0){
            if(columnNumber%26==0){
                title.append('Z');
                columnNumber=columnNumber/26-1;
            }else{
                title.append((char)(64+columnNumber%26));
                columnNumber/=26;
            }
        }
        title.reverse();
        return title.toString();
    }
}