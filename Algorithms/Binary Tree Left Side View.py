def LeftView(root):
    def l(root,level):
        if root==None:
            return
        if level not in dic:
            dic[level]=None
            result.append(root.data)
        l(root.left,level+1)
        l(root.right,level+1)
        
    dic={}  
    result=[]
    l(root,1)
    return result