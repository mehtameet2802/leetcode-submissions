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
    TreeNode* merge(TreeNode*&root1, TreeNode*&root2){
        TreeNode* y = new TreeNode(0);
        if(root1==NULL)
            y->val = root2->val;
        else if(root2==NULL)
            y->val = root1->val;
        else if(root1==NULL && root2==NULL)
            y = NULL;
        else
            y->val = root1->val+root2->val;
        return y;
    }

    void dfs(TreeNode*&root3,TreeNode*&root1, TreeNode*&root2){
        TreeNode* x = merge(root1,root2);
        root3 = x;
        // if(root1==NULL && root2 == NULL)
        //     return;
        if(root1!=NULL && root1->left!=NULL || root2!=NULL && root2->left!=NULL){
            if(root1==NULL)
                dfs(root3->left,root1,root2->left);
            else if(root2==NULL)
                dfs(root3->left,root1->left,root2);
            else
                dfs(root3->left,root1->left,root2->left);
        }
            
        if(root1!=NULL && root1->right!=NULL || root2!=NULL && root2->right!=NULL){
            if(root1==NULL)
                dfs(root3->right,root1,root2->right);
            else if(root2==NULL)
                dfs(root3->right,root1->right,root2);
            else
                dfs(root3->right,root1->right,root2->right);
        }
        return;
    }

    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if(root1==NULL && root2==NULL)
            return NULL;
        if(root1==NULL)
            return root2;
        if(root2==NULL)
            return root1;
        
        TreeNode* temp1 = root1;
        TreeNode* temp2 = root2;
        TreeNode* root3 = NULL;
        dfs(root3,temp1,temp2);
        return root3;
    }
};