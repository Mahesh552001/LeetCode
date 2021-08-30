class Solution {
    public void setZeroes(int[][] matrix) {
        int r=matrix.length;
        int c=matrix[0].length;
        int[] rows=new int[r];
        int[] cols=new int[c];
    
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if (matrix[i][j]==0){
                    rows[i]=1;
                    cols[j]=1;
                }
            }
        }
        for(int i=0;i<r;i++){
            if (rows[i]==1){
                for(int j=0;j<c;j++){
                    matrix[i][j]=0;
                }
            }
        }
        for(int i=0;i<c;i++){
            if (cols[i]==1){
                for(int j=0;j<r;j++){
                    matrix[j][i]=0;
                }
            }
        } 
    }
}