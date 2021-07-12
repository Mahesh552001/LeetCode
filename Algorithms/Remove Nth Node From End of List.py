# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow=head
        fast=head
        while(n>0):
            if fast.next!=None:
                fast=fast.next
                n-=1
            else:
                return head.next
        while(fast.next!=None):
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head