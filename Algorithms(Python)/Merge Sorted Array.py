class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i=0
        j=0
        
        while(i<m+n and j<n):
            if nums1[i]>nums2[j]:
                nums1[m+j]=nums2[j]
                nums1[i],nums1[m+j]=nums1[m+j],nums1[i]
                temp=m+j
                while(temp>i):
                    if nums1[temp]<nums1[temp-1]:
                        nums1[temp],nums1[temp-1]=nums1[temp-1],nums1[temp]
                    temp-=1
                j+=1
            i+=1
        for k in range(j,n):
            nums1[m+k]=nums2[k]
            if nums1[m+k-1]>nums1[m+k]:
                nums1[m+k-1],nums1[m+k]=nums1[m+k],nums1[m+k-1]