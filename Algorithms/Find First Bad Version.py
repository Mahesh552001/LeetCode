class Solution:
    def firstBadVersion(self, n):
        beg=1
        end=n
        while(beg<=end):
            mid=(beg+end)//2
            if (isBadVersion(mid) and (not isBadVersion(mid-1))):
                return mid
            if isBadVersion(mid):
                end=mid-1
            else:
                beg=mid+1