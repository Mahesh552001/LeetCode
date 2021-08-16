class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        n=len(s)
        start=0
        result=0
        for i in range(n):
            if s[i] in d:
                start=max(start,d[s[i]]+1)
            result=max(result,i-start+1)
            d[s[i]]=i
        return result