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
    vector<TreeNode*> bfs(TreeNode* root){
        queue<TreeNode*> q1;
        vector<TreeNode*> v1;
        q1.push(root);
        q1.push(NULL);
        while(!q1.empty()){
            TreeNode* front = q1.front();
            q1.pop();
            v1.push_back(front);
            if(front!=NULL){
                q1.push(front->left);
                q1.push(front->right);
            }
        }
        return v1;
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p==NULL && q==NULL)
            return true;
        
        if(p==NULL && q!=NULL || q==NULL && p!=NULL)
            return false;
        
        vector<TreeNode*> v1 = bfs(p);
        vector<TreeNode*> v2 = bfs(q);

        if(v1.size()!=v2.size())
            return false;
        
        for(int i=0;i<v1.size();i++){
            if(v1[i]==NULL && v2[i]==NULL)
                continue;
            else if(v1[i]!=NULL && v2[i]==NULL || v1[i]==NULL && v2[i]!=NULL)
                return false;
            else if(v1[i]->val != v2[i]->val)
                return false;
        }

        return true;


    }
};