class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=len(matrix)
        c=len(matrix[0])
        top=0;left=0;bottom=r-1;right=c-1
        result=[]
        while(top<=bottom and left<=right):
            self.lefttoright(matrix,top,left,right,result)
            self.toptobottom(matrix,right,top+1,bottom,result)
            if (top!=bottom and left!=right):
                self.righttoleft(matrix,bottom,right-1,left,result)
                self.bottomtotop(matrix,left,bottom-1,top+1,result)
            top+=1
            right-=1
            bottom-=1
            left+=1
        return result
            
    def lefttoright(self,matrix,row,start,end,result):
        for col in range(start,end+1):
            result.append(matrix[row][col])
    
    def toptobottom(self,matrix,col,start,end,result):
        for row in range(start,end+1):
            result.append(matrix[row][col])
            
    def righttoleft(self,matrix,row,start,end,result):
        for col in range(start,end-1,-1):
            result.append(matrix[row][col])
    
    def bottomtotop(self,matrix,col,start,end,result):
        for row in range(start,end-1,-1):
            result.append(matrix[row][col])