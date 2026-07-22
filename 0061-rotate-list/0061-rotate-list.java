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
    public ListNode kthNode(ListNode head,int k){
        ListNode temp=head;
        int cnt=1;
        while(temp!=null){
            if(cnt==k) return temp;
            cnt++;
            temp=temp.next;
        }
        return temp;
    }
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode tail=head;
        int length=1;
        while(tail.next!=null){
            length++;
            tail=tail.next;
        }
        
        if(k%length==0){
            return head;
        }
        k=k%length;
        tail.next=head;
        ListNode newlastnode=kthNode(head,length-k);
        head=newlastnode.next;
        newlastnode.next=null;
        return head;
        
    }
}