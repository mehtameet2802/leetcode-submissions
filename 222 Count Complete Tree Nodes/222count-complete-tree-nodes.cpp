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
    int leftHeight(TreeNode* root){
        int hgt = 0;
        while(root){
            hgt++;
            root = root->left;
        }
        return hgt;
    }

    int rightHeight(TreeNode* root){
        int hgt = 0;
        while(root){
            hgt++;
            root = root->right;
        }
        return hgt;
    }

    int solve(TreeNode* root){
        if(!root)
            return 0;
        
        int lft = leftHeight(root);
        int rgt = rightHeight(root);

        if(lft == rgt){
            return pow(2,lft)-1;
        }

        return 1+solve(root->left)+solve(root->right);
    }

    int countNodes(TreeNode* root) {
        return solve(root);
    }
};