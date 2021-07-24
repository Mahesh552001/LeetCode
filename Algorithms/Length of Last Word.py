class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        check=0
        for i in range(len(s)):
            if (s[i]==' '):
                if not check:
                    prev=l
                l=0
                check=1
            else:
                check=0
                l+=1
        if check:
            return prev
        return l