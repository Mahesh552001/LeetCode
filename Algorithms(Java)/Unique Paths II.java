class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows=obstacleGrid.length;
        int cols=obstacleGrid[0].length;
        if (obstacleGrid[0][0]==1){
            return 0;
        }
        obstacleGrid[0][0]=1;
        for(int row=1;row<rows;row++){
            obstacleGrid[row][0]=(obstacleGrid[row-1][0]==1 && obstacleGrid[row][0]==0)?1:0;
        }
        for(int col=1;col<cols;col++){
            obstacleGrid[0][col]=(obstacleGrid[0][col-1]==1 && obstacleGrid[0][col]==0)?1:0;
        }
        for(int row=1;row<rows;row++){
            for(int col=1;col<cols;col++){
                if(obstacleGrid[row][col]==1){
                    obstacleGrid[row][col]=0;
                }else{
                    obstacleGrid[row][col]=obstacleGrid[row-1][col]+obstacleGrid[row][col-1];
                }
            }
        }
        return obstacleGrid[rows-1][cols-1];
    }
}
