class Solution {
    public String convert(String s, int numRows) {
        if (numRows==1){
            return s;
        }
        int n=s.length();
        int col=0,temp=0;
        while(temp<=n){
            if (col==0 || col%(numRows-1)==0){
                temp+=numRows;
            }else{
                temp++;
            }
            col++;
        }
        System.out.println(col);
        char[][] matrix=new char[numRows][col];
        for(int c=0,i=0;c<col;c++){
            if (c==0 || c%(numRows-1)==0){
                for(int r=0;r<numRows;r++){
                    if(i<n){
                        matrix[r][c]=s.charAt(i);
                        i++;
                    }
                }
            }else if(i<n){
                matrix[numRows-1-(c%(numRows-1))][c]=s.charAt(i);
                i++;
            }
        }
        StringBuilder ans=new StringBuilder();
        for(int r=0;r<numRows;r++){
            for(int c=0;c<col;c++){
                if (matrix[r][c]!='\0'){
                    ans.append(matrix[r][c]);
                }
            }
        }
        return ans.toString();
    }
}