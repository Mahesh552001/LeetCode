class Solution {
    public String countAndSay(int n) {
        if(n == 1) return "1";
        if(n == 2) return "11";

        StringBuilder sb = new StringBuilder();
        String s = "11";
        for(int i = 3; i <=n; i++){
            sb.setLength(0);
            char temp = s.charAt(0);
            int count = 1;
            char curr = ' ';
            for(int j = 1; j < s.length(); j++){
                curr = s.charAt(j);
                if(curr != temp){
                    sb.append(count);
                    sb.append(temp);
                    temp = curr;
                    count = 1;
                }else{
                    count++;
                }
            }
            sb.append(count);
            sb.append(curr);
            
            s = sb.toString();
        }
        return s;
    }
}

//or

class Solution {
    public String countAndSay(int n) {
        if (n==1) return "1";
        if (n==2) return "11";
        String s="11";
        String sb="";
        for(int i=3;i<=n;i++){
            char temp=s.charAt(0);
            int count=1;
            sb="";
            int j=1;
            char curr=' ';
            for(;j<s.length();j++){
                curr=s.charAt(j);
                if (curr!=temp){
                    sb+=count;
                    sb+=temp;
                    temp=curr;
                    count=1;
                }else{
                    count++;
                }
            }
            sb+=count;
            sb+=curr;
            s=sb;
        }
        return s;
    }
}