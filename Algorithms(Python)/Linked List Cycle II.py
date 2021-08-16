class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        found=False
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                found=True
                break
        if not found:
            return None
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow

#OR

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        temp=head
        d={}
        while(temp):
            if temp in d:
                return temp
            d[temp]=None
            temp=temp.next
        return None