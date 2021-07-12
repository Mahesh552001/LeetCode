# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1=l1
        temp2=l2
        l3=ListNode()
        temp3=l3
        carry=0
        while(temp1 or temp2):
            x=temp1.val if temp1!=None else 0
            y=temp2.val if temp2!=None else 0
            s=x+y+carry
            carry=s//10
            temp3.next=ListNode(s%10)
            temp3=temp3.next
            if temp1!=None:temp1=temp1.next
            if temp2!=None:temp2=temp2.next
        if carry>0:
            temp3.next=ListNode(carry)
        return l3.next