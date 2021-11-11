class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode newHead=new ListNode(-1);
        newHead.next=head;
        ListNode temp=newHead;
        while(temp!=null && temp.next!=null){
            if(temp.next.val==val){
                temp.next=temp.next.next;
            }else{
                temp=temp.next;
            }
        }
        return newHead.next;
    }
}

//other approach-Python
/*class Solution:
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
        return head */