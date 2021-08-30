/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head==null){
            return head;
        }
        Node copy=new Node(-1);
        Node temp=head;
        Node c=copy;
        HashMap<Node,Node> h=new HashMap<Node,Node>();
        while(temp!=null){
            c.next=new Node(temp.val);
            h.put(temp,c.next);
            c=c.next;
            temp=temp.next;
        }
        temp=head;
        c=copy.next;
        while(temp!=null){
            c.random=temp.random!=null?h.get(temp.random):null;
            temp=temp.next;
            c=c.next;
        }
        return copy.next;
    }
}