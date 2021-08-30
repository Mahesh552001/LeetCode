/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        LinkedList<Integer> ll=new LinkedList<>();
        ListNode temp=head;
        while(temp!=null){
            ll.addLast(temp.val);
            temp=temp.next;
        }
        temp=head;
        while(temp!=null){
            if (temp.val!=ll.removeLast()){
                return false;
            }
            temp=temp.next;
        }
        return true;
    }
}

//or

//Efficient
class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null){
            return true;
        }
        ListNode slow = head;
        ListNode fast = head;
        
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        ListNode second = reverse(slow.next);
        ListNode first = head;
        while(first != null && second != null){
            if(first.val != second.val){
                return false;
            }
            first = first.next;
            second = second.next;
        }
        return true;
    }
    
    public ListNode reverse(ListNode node){
        ListNode prev = null;
        ListNode curr = node;
        
        while(curr != null){
            ListNode next= curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}