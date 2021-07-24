def tri(arr,n):
    if n!=1:
        arr1=arr.copy()
        arr1=arr1[0:n-1]
        for i in range(n-1):
            arr1[i]+=arr[i+1]
        tri(arr1,n-1)
    print (arr)
arr=list(map(int,input().split()))
tri(arr,len(arr))

def power(x,y):
    temp = 0
    if( y == 0):
        return 1
    temp = power(x, int(y/2))
    if (y % 2 == 0):
        return temp * temp;
    else:
        return x * temp * temp;
         #else: return (temp * temp) / x (if y <0)
     
x, y = 2,4
print('%.6f' %(power(x, y)))

def sortInWave(arr, n):
     
    # Traverse all even elements
    for i in range(0, n, 2):
         
        # If current even element is smaller than previous
        if (i> 0 and arr[i] < arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
         
        # If current even element is smaller than next
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
 
# Driver program
arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
for i in range(0,len(arr)):
    print (arr[i])
    
    
    
def Square(n, i, j):
    mid = (i + j) / 2;
    mul = mid * mid;
    if ((mul == n) or (abs(mul - n) < 0.00001)):
        return mid;
    elif (mul < n):
        return Square(n, mid, j);
    else:
        return Square(n, i, mid);
def findSqrt(n):
    i = 1;
    found = False;
    while (found == False):
        if (i * i == n):
            print(i);
            found = True;    
        elif (i * i > n):
            res = Square(n, i - 1, i);
            print ("{0:.5f}".format(res))
            found = True
        i += 1;
# Driver code
if __name__ == '__main__':
    n = 3;
    findSqrt(n);
    
    
s=list(input().lower())
for i in range(1,len(s)):
    if s[i]=='x' and s[i-1]=='y':
        s[i],s[i-1]=s[i-1],s[i]
print(s)