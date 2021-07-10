class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        temp=head
        l=0
        while(temp):
            l+=1
            temp=temp.next
        k=k%l
        if k==0:
            return head
        temp=head
        for i in range(k):
            while(temp.next.next!=None):
                temp=temp.next
            next=head
            head=temp.next
            temp.next=None
            head.next=next
            temp=head
        return head