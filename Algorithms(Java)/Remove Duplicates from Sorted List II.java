class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode ll=new ListNode(-100);
        ll.next=head;
        ListNode temp=ll;
        while(temp.next!=null && temp.next.next!=null){
            if (temp.next.val==temp.next.next.val){
                int num=temp.next.val;
                while(temp.next!=null && temp.next.val==num){
                    temp.next=temp.next.next;
                }
                continue;
            }
            temp=temp.next;
        }
        return ll.next;
    }
}