class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        temp=head
        count=1
        if count==left:
            return self.reverse(head,right-left)
        while(temp):
            if count+1==left:
                temp.next=self.reverse(temp.next,right-left)
                return head
            count+=1
            temp=temp.next
        
    def reverse(self,head,s):
        temp=head
        
        for i in range(s):
            temp=temp.next
        prev=temp.next
        
        curr=head
        while(curr and s>-1):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            s-=1
        temp2=prev
        return prev