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

    pair<int,bool> check(TreeNode* root){
        if(root == NULL)
            return {0,true};
        
        if(root->left==NULL && root->right==NULL)
            return {1,true};
        
        pair<int,bool> left = check(root->left);
        pair<int,bool> right = check(root->right);
        
        if(left.second==false || right.second==false)
            return {-1,false};
        
        if(abs(left.first-right.first)>1)
            return {-1,false};
        
        int x = max(left.first,right.first)+1;
        return {x,true};
    }

    bool isBalanced(TreeNode* root) {
        pair<int,bool> ans = check(root);
        return ans.second;
    }
};