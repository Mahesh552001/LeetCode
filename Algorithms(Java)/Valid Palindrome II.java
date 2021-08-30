class Solution {
    public boolean validPalindrome(String s) {
        int n=s.length();
        char[] arr=s.toCharArray();
        int i=0,j=n-1,left=0,right=0;
        boolean changed=false;
        boolean equals=false,needed=false;
        
        while(i<=j){
            if (arr[i]!=arr[j]){
                if (changed && !equals){
                    return false;
                }else if(changed &&  equals){
                    needed=true;
                    break;
                }else{
                    if ((arr[i]==arr[j-1])&&(arr[j]==arr[i+1])){
                        equals=true;
                        left=i;
                        right=j;
                        i++;
                    }else if (arr[i]==arr[j-1]){
                        j--;
                    }else{
                        i++;
                    }
                    changed=true;
                    continue;
                }
            }
            i++;j--;
        }
        if (equals && needed){
            right--;
            while(left<=right){
                if(arr[left]!=arr[right]){
                    return false;
                }
                left++;right--;
            }
        }
        return true;
    }
}