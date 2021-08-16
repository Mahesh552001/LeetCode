class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None:
            return head
        copy=Node(head.val)
        temp=head.next
        c=copy
        while(temp):
            c.next=Node(temp.val)
            c=c.next
            temp=temp.next
        temp=head
        c=copy
        while(temp):
            next=temp.next
            temp.next=c
            c.random=temp.random
            c=c.next
            temp=next
        c=copy
        while(c):
            if c.random!=None:
                c.random=c.random.next
            c=c.next
        return copy