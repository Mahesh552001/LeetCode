https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1#


/*
class Node
{
    int data;
    Node next;
}
*/

class Solution
{
    //Function to remove a loop in the linked list.
    public static void removeLoop(Node head){
       boolean check=true;
       Node slow=head;
       Node fast=head;
       while(fast!=null && fast.next!=null){
           slow=slow.next;
           fast=fast.next.next;
           if (slow==fast){
               check=false;
               break;
           }
       }
       if (check){
           return;
       }
       else{
           slow=head;
           while(slow!=fast){
               slow=slow.next;
               fast=fast.next;
           }
           while(fast.next!=slow){
               fast=fast.next;
           }
           fast.next=null;
       }
       return;
    }
}