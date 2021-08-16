class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        arr=[]
        for i in s:
            arr.append(d[i])
        answer=arr[0]
        i=1
        while i<len(arr):
            if arr[i-1]<arr[i]:
                answer+=arr[i]-arr[i-1]-arr[i-1]
            else:
                answer+=arr[i]
            i+=1
        return answer

#OR

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        n = len(s)
        total = dic[s[n-1]]
        for i in range(n-1,0,-1):
            current = dic[s[i]]
            prev = dic[s[i-1]]
            total += prev if prev >= current else -prev
        return total
