# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        l=0
        temp=head
        while(temp):
            l+=1
            temp=temp.next
        s1=l%k
        s2=l//k
        output=[]
        temp=head
        for i in range(k):
            head=ListNode()
            ll=head
            if i<s1:
                for j in range(s2+1):
                    ll.next=ListNode(temp.val)
                    temp=temp.next
                    ll=ll.next
            else:
                for j in range(s2):
                    ll.next=ListNode(temp.val)
                    temp=temp.next
                    ll=ll.next
            output.append(head.next)
        return output
    