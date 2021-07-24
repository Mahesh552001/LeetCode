class Solution:
    def compress(self, arr: List[str]) -> int:
        count=1
        ind=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                count+=1
            else:
                if count>1:
                    for k in str(count):
                        arr[ind]=k
                        ind+=1
                arr[ind]=arr[i]
                count=1
                ind+=1
        if count>1:
            for i in str(count):
                arr[ind]=i
                ind+=1
        return ind