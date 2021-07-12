#Iterative Approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        current=head
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        head=prev
        return head

#OR

#Recursive Approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        return self.reverse(head,None)
    
    def reverse(self,curr,prev):
        if curr.next==None:
            curr.next=prev
            return curr
        next=curr.next
        curr.next=prev
        return self.reverse(next,curr)
        