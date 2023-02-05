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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(root == NULL)
            return ans;

        queue<TreeNode*> q1;
        vector<TreeNode*> v1;
        q1.push(root);
        q1.push(NULL);
        while(!q1.empty()){
            TreeNode* first = q1.front();
            q1.pop();
            v1.push_back(first);
            if(first!=NULL && first->left!=NULL)
                q1.push(first->left);
            if(first!=NULL && first->right!=NULL)
                q1.push(first->right);
            if(first==NULL && !q1.empty())
                q1.push(NULL);
        }

        vector<int> v2;
        for(int i=0;i<v1.size();i++){
            if(v1[i] == NULL){
                ans.push_back(v2);
                v2.clear();
            }
            else{
                v2.push_back(v1[i]->val);
            }
            
        }
        return ans;
    }
};