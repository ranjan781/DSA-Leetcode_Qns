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
    int maxi=INT_MIN;
private:
    int helper(TreeNode* node){
        if(node==nullptr) return 0;
        int leftsum=max(0,helper(node->left));
        int rightsum=max(0,helper(node->right));
        maxi=max(maxi,node->val+leftsum+rightsum);
        return node->val+max(leftsum,rightsum);

    }
public:
    int maxPathSum(TreeNode* root) {
        if(root==nullptr) return 0;
        helper(root);
        return maxi;
    }
};