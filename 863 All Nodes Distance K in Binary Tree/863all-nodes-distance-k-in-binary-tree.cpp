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
    map<int,vector<int>> mp;
    map<int,bool> mp1;
    vector<int> ans;

    void create(TreeNode* root){
        if(!root)
            return;
    
        if(root->left){
            mp[root->val].push_back(root->left->val);
            mp[root->left->val].push_back(root->val);
            create(root->left);
        }

        if(root->right){
            mp[root->val].push_back(root->right->val);
            mp[root->right->val].push_back(root->val);
            create(root->right);
        }
    }

    void reach(int root, int k){
        if(k==0){
            ans.push_back(root);
            return;
        }
    
        for(auto it:mp[root]){
            if(!mp1[it]){
                mp1[it] = true;
                reach(it,--k);
                k++;
                mp1[it] = false;
            }
        }
    }

    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        if(k==0)
            return {target->val};
        create(root);
        mp1[target->val] = true;
        for(auto it:mp[target->val]){
            mp1[it] = true;
            reach(it,--k);
            k++;
            mp1[it] = false;
        }
        return ans;
    }
};