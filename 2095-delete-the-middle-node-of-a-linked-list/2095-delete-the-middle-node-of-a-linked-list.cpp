/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if(head->next==nullptr){
            return nullptr;
        }
        ListNode* slow=head;
        ListNode* fast=slow->next->next;
        while(fast!=nullptr && fast->next!=nullptr){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* temp=slow->next;
        slow->next=slow->next->next;
        temp->next=nullptr;
        delete temp;
        return head;
    
    }
};