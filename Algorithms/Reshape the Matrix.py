class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if (m*n)!=(r*c):
            return mat
        else:
            linear=[]
            for i in range(m):
                for j in range(n):
                    linear.append(mat[i][j])
            newmat=[]
            ind=0
            for i in range(r):
                temp=[]
                for j in range(c):
                    temp.append(linear[ind])
                    ind+=1
                newmat.append(temp)
            return newmat