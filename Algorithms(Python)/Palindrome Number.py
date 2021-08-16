class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        
        if x[::-1]==x:
            return True
        else:
            return False

#OR

#better use this
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:
            return True
        elif x>0:
            temp=x
            rev=0
            while temp!=0:
                rem=temp%10
                rev=(rev*10)+rem
                temp//=10
            if x==rev:
                return True
            return False
        return False

#OR
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        l=len(x)
        for i in range(l//2):
            if x[i]!=x[l-1-i]:
                return False
        return True