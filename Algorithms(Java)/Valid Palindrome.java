class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        char[] ch=s.toCharArray();
        int n=s.length();
        int i=0,j=n-1;
        while(i<=j){
            if (!isAlphanumeric(ch[i])){
                i++;
                continue;
            }
            if (!isAlphanumeric(ch[j])){
                j--;
                continue;
            }
            if (ch[i]!=ch[j]){
                return false;
            }
            i++;j--;
        }
        return true;
    }
    public boolean isAlphanumeric(char c){
        if ((c>='A' && c<='Z') || (c>='a' && c<='z') || (c>='0' && c<='9')){
            return true;
        }
        return false;
    }
}