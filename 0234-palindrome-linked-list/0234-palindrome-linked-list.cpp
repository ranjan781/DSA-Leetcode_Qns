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
    bool isPalindrome(ListNode* head) {
        stack<int>stack;
        ListNode* temp=head;
        while(temp){
            stack.push(temp->val);
            temp=temp->next;
        }
        temp=head;
        while(temp){
            if(temp->val==stack.top() && temp){
                stack.pop();
                temp=temp->next;
            }else{
                return false;
            }
        }
        return true;
        
    }
};