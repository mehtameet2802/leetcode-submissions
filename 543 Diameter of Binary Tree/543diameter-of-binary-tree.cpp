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
    int ans = INT_MIN;
    
    int check(TreeNode* root){
        if(!root)
            return 0;
        
        int left = check(root->left);
        int right = check(root->right);
        int d = left+right+1;
        ans = max(d,ans);
        int a1 = max(left,right)+1;
        return a1;
    }

    int diameterOfBinaryTree(TreeNode* root) {
        int x = check(root);
        return ans-1;
    }
};