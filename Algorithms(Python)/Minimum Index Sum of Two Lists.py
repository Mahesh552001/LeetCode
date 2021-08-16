class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        for i in range(len(list1)):
            if list1[i] in list2:
                d[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] in d:
                d[list2[i]]+=i
        d=sorted(d.items(),key=lambda x:x[1])
        val=d[0][1]
        arr=[]
        for i in d:
            x,y=i
            if y==val:
                arr.append(x)
        return arr