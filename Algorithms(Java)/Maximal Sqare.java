class Solution {
    public int maximalSquare(char[][] matrix) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        int[][] table=new int[rows+1][cols+1];
        int size=0;
        for(int row=1;row<=rows;row++){
            for(int col=1;col<=cols;col++){
                if(matrix[row-1][col-1]=='1'){
                    table[row][col]=Math.min(table[row-1][col-1],
                                             Math.min(table[row-1][col],table[row][col-1]))+1;
                    size=Math.max(size,table[row][col]);
                }
            }
        }
        return size*size;
    }
}