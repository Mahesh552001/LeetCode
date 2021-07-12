class Solution {
    public double myPow(double x, long n) {
        if (n==0 || x==1){
            return 1;
        }
        if (n<0){
            return myPow(1/x,-n);
        }
        double temp=myPow(x,n/2);
        if (n%2==0){
            return temp*temp;
        }else{
            return x*temp*temp;
        }
    }
}