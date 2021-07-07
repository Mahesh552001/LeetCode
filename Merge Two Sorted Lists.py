# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1=l1
        temp2=l2
        l3=ListNode()
        temp3=l3
        while(temp1 or temp2):
            if temp1==None and temp2!=None:
                temp3.next=temp2
                return l3.next
            elif temp2==None and temp1!=None:
                temp3.next=temp1
                return l3.next
            elif temp1.val<=temp2.val:
                temp3.next=ListNode(temp1.val)
                temp3=temp3.next
                if temp1!=None:temp1=temp1.next
            else:
                temp3.next=ListNode(temp2.val)
                temp3=temp3.next
                if temp2!=None:temp2=temp2.next
        return l3.next