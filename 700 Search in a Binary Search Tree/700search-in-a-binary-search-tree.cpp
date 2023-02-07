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
    TreeNode* sear(TreeNode*root,int val){
        if(root == NULL)
            return NULL;
        if(root->val == val)
            return root;
        TreeNode* left = sear(root->left,val);
        TreeNode* right = sear(root->right,val);
        if(left!=NULL && left->val == val)
            return left;
        else if(right!=NULL && right->val == val)
            return right;
        return NULL;
    }
    TreeNode* searchBST(TreeNode* root, int val) {
        return sear(root,val);
    }
};