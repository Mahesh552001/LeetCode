class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        int l=0,r=rows-1,mid=0,search=0;
        while(l<=r){
            mid=(l+r)/2;
            if(matrix[mid][0]>target){
                r=mid-1;
            }else{
                l=mid+1;
                search=l-1;
            }
        }
        System.out.println(search);
        l=0;r=cols-1;
        while(l<=r){
            mid=(l+r)/2;
            if(matrix[search][mid]==target){
                return true;
            }else if(matrix[search][mid]<target){
                l=mid+1;
            }else{
                r=mid-1;
            }
        }
        return false;
    }
}