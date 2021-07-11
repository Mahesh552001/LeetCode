class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return self.toBinary(self.toDecimal(int(a))+self.toDecimal(int(b)))
        
    def toDecimal(self,x):
        if x==0:return 0
        d=0
        base=1
        while(x>0):
            rem=x%10
            d+=rem*base
            base*=2
            x//=10
        return d
    
    def toBinary(self,x):
        if x==0:return '0'
        arr=[]
        while(x>0):
            if x%2==0:
                arr.append('0')
            else:
                arr.append('1')
            x//=2
        arr.reverse()
        return "".join(arr)
        