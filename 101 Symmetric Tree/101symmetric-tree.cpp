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

    void bfs1(TreeNode* root, vector<TreeNode*> &v){
        queue<TreeNode*> q1;
        q1.push(root);
        while(!q1.empty()){
            TreeNode* first = q1.front();
            q1.pop();
            v.push_back(first);
            if(first!=NULL){
                q1.push(first->left);
                q1.push(first->right);
            }
        }
    }

    void bfs2(TreeNode* root, vector<TreeNode*> &v){
        queue<TreeNode*> q1;
        q1.push(root);
        while(!q1.empty()){
            TreeNode* first = q1.front();
            q1.pop();
            v.push_back(first);
            if(first!=NULL){
                q1.push(first->right);
                q1.push(first->left);
            }
        }
    }

    bool isSymmetric(TreeNode* root) {
        if(root->left==NULL && root->right==NULL)
            return true;
        if(root->left==NULL || root->right==NULL)
            return false;
        vector<TreeNode*> v1;
        vector<TreeNode*> v2;
        bfs1(root->left,v1);
        bfs2(root->right,v2);

        if(v1.size()!=v2.size())
            return false;
        for(int i=0;i<v1.size();i++){
            if(v1[i]==NULL && v2[i]==NULL)
                continue;
            else if(v2[i]==NULL || v1[i]==NULL)
                return false;
            else if(v1[i]->val != v2[i]->val)
                return false;
        }
        return true;
    }
};