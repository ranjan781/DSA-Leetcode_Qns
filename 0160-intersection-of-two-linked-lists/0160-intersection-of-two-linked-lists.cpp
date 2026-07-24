/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* collison(ListNode* t1,ListNode* t2,int d){
        while(d){
            d--;
            t2=t2->next;
        }
        while(t1!=t2){
            t1=t1->next;
            t2=t2->next;
        }
        return  t1;
    };
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* t1=headA;
        ListNode* t2=headB;
        int cnt1=0;
        int cnt2=0;
        while(t1->next!=nullptr){
            cnt1++;
            t1=t1->next;
        }
        while(t2->next!=nullptr){
            cnt2++;
            t2=t2->next;
        }
        if(cnt2>=cnt1){
            return collison(headA,headB,cnt2-cnt1);
        }else{
            return collison(headB,headA,cnt1-cnt2);
        }
        return nullptr;
    }
};