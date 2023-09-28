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
    vector<int> ans;
    stack<TreeNode*> st;

    void solve(){
        if(st.empty())
            return;
        TreeNode* t1 = st.top();
        st.pop();
        ans.push_back(t1->val);
        if(t1->right!=NULL)
            st.push(t1->right);
        if(t1->left!=NULL)
            st.push(t1->left);
        solve();
    }

    vector<int> preorderTraversal(TreeNode* root) {
        if(!root)
            return ans;
        st.push(root);
        solve();
        return ans;
    }
};