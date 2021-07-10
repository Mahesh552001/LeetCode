class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        odd_head=head
        even_head=head.next
        odd=odd_head
        even=even_head
        while(even and even.next):
            odd.next=even.next
            even.next=even.next.next
            odd=odd.next
            even=even.next  
        odd.next=even_head
        return odd_head 