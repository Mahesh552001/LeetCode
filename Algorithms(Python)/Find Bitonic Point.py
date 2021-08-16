#https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1/?company[]=Amazon&company[]=Amazon&problemStatus=solved&problemType=functional&page=1&sortBy=submissions&query=company[]AmazonproblemStatussolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazon
#geeksforgeeks

class Solution:
	def findMaximum(self,arr,n):
	    start=0
	    end=n-1
	    while(start<=end):
	        mid=(start+end)//2
	        if (mid==0 or mid==n-1 or (arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1])):
	            return arr[mid]
	        if (arr[mid]<arr[mid+1]):
	            start=mid+1
	        else:
	            end=mid-1