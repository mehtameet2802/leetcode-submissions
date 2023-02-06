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
    bool check(TreeNode* root, int targetSum,int sum){
        if(root==NULL)
            return false;
        if(root->left==NULL && root->right==NULL){
            sum = sum+root->val;
            if(sum == targetSum)
                return true;
        }
        bool left = check(root->left,targetSum,sum+root->val);
        bool right = check(root->right,targetSum,sum+root->val);
        return left||right;
    }
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root==NULL)
            return false;
        return check(root,targetSum,0);
    }
};