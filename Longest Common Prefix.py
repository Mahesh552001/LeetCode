class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        index=0
        while True:
            if index>len(strs[0])-1:
                return ans
            s=strs[0][index]
            for i in strs:
                if index>len(i)-1:
                    return ans
                if i[index]!=s:
                    return ans
            ans+=s
            index+=1