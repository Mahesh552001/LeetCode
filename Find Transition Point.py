#https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1/?company[]=Amazon&company[]=Amazon&problemStatus=solved&problemType=functional&page=1&sortBy=submissions&query=company[]AmazonproblemStatussolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazon
#Geeksforgeeks

def transitionPoint(arr, n):
    beg=0
    end=n-1
    if n==1:
        if arr[0]==0:
            return -1
        return 0
    flag=0
    while(beg<=end):
        mid=(beg+end)//2
        if (arr[mid]==1 and arr[mid-1]==0):
            return mid
        elif (arr[mid]==1):
            end=mid-1
            flag=1
        else:
            beg=mid+1
    if flag==0:
        return -1
    return 0
