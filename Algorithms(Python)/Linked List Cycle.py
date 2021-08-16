class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

#OR

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow=head
        fast=head.next
        while(slow!=fast):
            if fast==None or fast.next==None:
                return False
            slow=slow.next
            fast=fast.next.next
        return True

#OR

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d={}
        temp=head
        while(temp):
            if temp in d:
                return True
            else:
                d[temp]=None
            temp=temp.next
        return False
