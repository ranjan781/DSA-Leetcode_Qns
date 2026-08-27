/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void rightside(TreeNode* curr,vector<int>&res,int currdepth){
        if(curr==nullptr) return;
        if(currdepth==res.size()){
            res.push_back(curr->val);
        }
        rightside(curr->right,res,currdepth+1);
        rightside(curr->left,res,currdepth+1);
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int>res;
        rightside(root,res,0);
        return res;
    }
};