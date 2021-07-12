class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        if l<2 or s==s[::-1]:
            return s
        matrix=[[False for i in range(l)] for i in range(l)]
        long_pal=s[0]
        i=0
        while(i<l):
            matrix[i][i]=True
            i+=1
        for i in range(l-1):
            if s[i]==s[i+1]:
                matrix[i][i+1]=True
                long_pal=s[i]+s[i+1]
        for i in range(2,l):
            for j in range(l-i):
                if s[j]==s[j+i] and matrix[j+1][j+i-1]:
                    matrix[j][j+i]=True
                    long_pal=s[j:j+i+1]
        return long_pal
                    