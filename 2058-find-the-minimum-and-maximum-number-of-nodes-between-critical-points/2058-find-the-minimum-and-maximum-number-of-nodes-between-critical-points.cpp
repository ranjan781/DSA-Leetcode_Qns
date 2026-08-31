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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int cnt=0;
        ListNode* curr=head;
        while(curr!=nullptr){
            cnt++;
            curr=curr->next;
        }
        if(cnt<=2) return {-1,-1};
        vector<int>vec;
        ListNode* temp=head;
        int x=0;
        while(temp!=NULL && temp->next!=NULL && temp->next->next!=NULL){
            x++;
            if((temp->val < temp->next->val && temp->next->val > temp->next->next->val) || (temp->val > temp->next->val && temp->next->val < temp->next->next->val)) 
            vec.push_back(x+1);

            temp=temp->next;
        }
        if(vec.size()<2) return {-1,-1};
        int mn=INT_MAX;
        for(int i=1;i<vec.size();i++){
            mn=min(mn,abs(vec[i]-vec[i-1]));
        }
        int mx=abs(vec[0]-vec[vec.size()-1]);

        return {mn,mx};
    }
};