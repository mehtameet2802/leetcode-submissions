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

    bool dfs(TreeNode*root,int x,vector<TreeNode*> &ans){
        if(root==NULL)
            return false;
        
        if(root->val==x){
            ans.push_back(root);
            return true;
        }
        
        bool a1 = dfs(root->left,x,ans);
        bool a2 = dfs(root->right,x,ans);
        
        if(a1==true || a2==true){
            ans.push_back(root);
            return true;
        }
        return false;
        
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> ans1;
        vector<TreeNode*> ans2;
        vector<TreeNode*> common;
        bool a1 = dfs(root,p->val,ans1);
        bool a2 = dfs(root,q->val,ans2);
        reverse(ans1.begin(),ans1.end());
        reverse(ans2.begin(),ans2.end());
        if(ans1.size()<=ans2.size()){
            for(int i=0;i<ans1.size();i++){
                if(ans1[i] == ans2[i])
                    common.push_back(ans1[i]);
            }
        }
        else{
            for(int i=0;i<ans2.size();i++){
                if(ans2[i] == ans1[i])
                    common.push_back(ans2[i]);
            }
        }
        return common[common.size()-1];
    }
};