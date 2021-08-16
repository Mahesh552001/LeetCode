class Solution:
    def customSortString(self, order: str, string: str) -> str:
        d={}
        for i in range(len(string)):
            if string[i] in d:
                d[string[i]]+=1
            else:
                d[string[i]]=1
        ans=""
        i=0
        while(i<len(order)):
            if order[i] in d:
                if d[order[i]]==1:
                    ans+=order[i]
                    del d[order[i]]
                else:
                    ans+=order[i]
                    d[order[i]]-=1
                    continue
            i+=1
        for k,v in d.items():
            ans+=k*v
        return ans