#https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1#
#GeeksforGeeks

class Solution:
    def findExtra(self,a,b,n):
        start=0
        end=n-1
        while(start<=end):
            mid=(start+end)//2
            if mid==n-1:
                return mid
            if a[mid]==b[mid]:
                start=mid+1
            else:
                end=mid-1
                ans=mid
        return ans