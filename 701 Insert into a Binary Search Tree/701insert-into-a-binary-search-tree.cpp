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
    void in(TreeNode*&root,int val){
        if(root->left==NULL && val<root->val){
            TreeNode* x = new TreeNode(val);
            root->left = x;
        }
        else if(root->right==NULL && val>root->val){
            TreeNode* x = new TreeNode(val);
            root->right = x;
        }
        if(val<root->val)
            in(root->left,val);
        else if(val>root->val)
            in(root->right,val);
    }
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(root == NULL){
            TreeNode* x = new TreeNode(val);
            root = x;
        }
        in(root,val);
        return root;
    }
};