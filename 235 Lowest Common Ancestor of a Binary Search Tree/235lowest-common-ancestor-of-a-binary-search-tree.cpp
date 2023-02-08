/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    void dfs(TreeNode*root,vector<TreeNode*>&v,int target){
        if(root == NULL)
            return;
        if(root->val == target){
            v.push_back(root);
            return;
        }
        v.push_back(root);
        if(root->val<target)
            dfs(root->right,v,target);
        else
            dfs(root->left,v,target);
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> v,v1,v2;
        TreeNode* ans;
        dfs(root,v1,p->val);
        dfs(root,v2,q->val);
        int i=0,j=0;
        while(i<v1.size() && j<v2.size()){
            if(v1[i] == v2[j])
                v.push_back(v1[i]);
            i++;
            j++;
        }
        ans = v[v.size()-1];

        return ans;
    }
};