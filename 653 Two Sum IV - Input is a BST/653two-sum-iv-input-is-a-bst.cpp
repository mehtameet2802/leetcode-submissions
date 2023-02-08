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
    void bfs(TreeNode* root,vector<TreeNode*>&v){
        queue<TreeNode*> q1;
        q1.push(root);
        while(!q1.empty()){
            TreeNode* first = q1.front();
            q1.pop();
            v.push_back(first);
            if(first!=NULL && first->left!=NULL)
                q1.push(first->left);
            if(first!=NULL && first->right!=NULL)
                q1.push(first->right);
            if(first!=NULL && !q1.empty())
                q1.push(NULL);
        }
    }
    bool findTarget(TreeNode* root, int k) {
        vector<int> v1;
        vector<TreeNode*> v;
        bfs(root,v);
        for(int i=0;i<v.size();i++){
            if(v[i]==NULL)
                continue;
            else{
                v1.push_back(v[i]->val);
            }
        }
        sort(v1.begin(),v1.end());
        map<int,int> mp;
        for(int i=0;i<v1.size();i++){
            if(mp[k-v1[i]] == 1)
                return true;
            else
                mp[v1[i]] = 1;
        }
        return false;
    }
};