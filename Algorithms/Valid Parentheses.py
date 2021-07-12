class Solution:
    def isValid(self, s: str) -> bool:
        d={"(":")","{":"}","[":"]"}
        stack=[]
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                elif d[stack.pop()]!=i:
                    return False
        return True if len(stack)==0 else False
                    