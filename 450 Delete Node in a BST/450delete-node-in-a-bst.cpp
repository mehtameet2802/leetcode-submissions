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
    TreeNode* suc(TreeNode * root){
        TreeNode*p = root->right;
        while(p->left)
            p = p->left;
        return p;
    }

    
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root) 
            return NULL;
        if(root->val<key) 
            root->right = deleteNode(root->right,key); 
        else if(root->val>key) 
            root->left = deleteNode(root->left,key); 
        else if(root->val == key){
            if(!root->right){
                TreeNode * temp = root->left;
                delete(root);
                return temp;
            }
            else if(!root->left){
                TreeNode * temp = root->right;
                delete(root);
                return temp;
            }
            else{
                TreeNode * temp = suc(root);
                swap(root->val,temp->val);
                root->right = deleteNode(root->right,key);
            }
        }
        return root;
    }
};