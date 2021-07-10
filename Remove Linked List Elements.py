# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while(head and head.val==val):
            head=head.next
        if head==None:
            return head
        temp=head
        while(temp and temp.next):
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
    