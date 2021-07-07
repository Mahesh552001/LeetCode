#better time complexity
class Solution:
    def getRow(self, n: int) -> List[int]:
        ans=[1]
        for i in range(1,n+1):
            if i==n:
                ans.append(1)
            else:
                ans.append(int((ans[i-1]*(n-(i-1))/i)))
        return ans

#OR

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr=[[1],[1,1]]
        for i in range(2,rowIndex+1):
            temp=[]
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(arr[i-1][j]+arr[i-1][j-1])
            arr.append(temp)
        return arr[rowIndex]