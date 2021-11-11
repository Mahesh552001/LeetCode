class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int r1=mat.length;
        int c1=mat[0].length;
        if (r1*c1!=r*c){
            return mat;
        }
        int[][] ans=new int[r][c];
        int m=0,n=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                ans[i][j]=mat[m][n];
                if (n<c1-1){
                    n++;
                }else{
                    n=0;
                    m++;
                }
            }
        }
        return ans;
    }
}

//or

class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
    int m = nums.length, n = nums[0].length;
    if (r * c != m * n)
        return nums;
    int[][] reshaped = new int[r][c];
    for (int i = 0; i < r * c; i++)
        reshaped[i/c][i%c] = nums[i/n][i%n];
    return reshaped;
 }
}

//  m[i][j] = m[n*i+j]  n-->no. of cols
//  m[i] = m[i/n][i%n]  n-->no. of cols