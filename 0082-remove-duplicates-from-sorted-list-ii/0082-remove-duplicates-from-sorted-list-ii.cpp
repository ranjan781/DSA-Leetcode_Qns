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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp=head;
        unordered_map<int,int> mp;
        while(temp!=NULL){
            mp[temp->val]++;
            temp=temp->next;
        }
        ListNode* dummy= new ListNode(0);
        ListNode* ans=dummy;
        ListNode* temp1=head;
        while(temp1!=NULL){
            if(mp[temp1->val]==1){ dummy->next=new ListNode(temp1->val); dummy=dummy->next;}
            temp1=temp1->next;
        }
        return ans->next;
    }
};