/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        boolean check=true;
        ListNode slow=head;
        ListNode fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
            if (slow==fast){
                check=false;
                break;
            }
        }
        if (check){
            return null;
        }
        else{
            slow=head;
            while(slow!=fast){
                slow=slow.next;
                fast=fast.next;
            }
            return slow;
        }
    }
}

//or

public class Solution {
    public ListNode detectCycle(ListNode head) {
        HashSet<ListNode> h=new HashSet<ListNode>();
        ListNode temp=head;
        while(temp!=null){
            if (h.contains(temp)){
                return temp;
            }
            h.add(temp);
            temp=temp.next;
        }
        return null;
    }
}
