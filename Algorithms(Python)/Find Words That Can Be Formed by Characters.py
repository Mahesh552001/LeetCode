class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:  
        ans=0
        for word in words:
            d={}
            for i in chars:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            l=0
            for ch in word:
                if ch in d and d[ch]>0:
                    d[ch]-=1
                    l+=1
                else:
                    break
            if l==len(word):
                ans+=l
        return ans
   