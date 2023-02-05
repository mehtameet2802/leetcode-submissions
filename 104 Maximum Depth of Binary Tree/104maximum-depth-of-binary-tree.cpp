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
    int dfs(TreeNode* root,int d){
        if(root == NULL)
            return 0;
        int d1 = d+1+dfs(root->left,d);
        int d2 = d+1+dfs(root->right,d);
        int depth = max(d1,d2);
        return depth;
    }
    int maxDepth(TreeNode* root) {
        int d = dfs(root,0);
        return d;
    }
};