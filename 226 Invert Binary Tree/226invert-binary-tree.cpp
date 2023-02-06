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
    // void bfs(TreeNode* root, vector<TreeNode*> &v){
    //     queue<TreeNode*> q1;
    //     q1.push(root);
    //     q1.push(NULL);
    //     while(!q1.empty()){
    //         TreeNode* first = q1.front();
    //         q1.pop();
    //         v.push_back(first);
    //         if(first!=NULL && first->left!=NULL)
    //             q1.push(first->left);
    //         if(first!=NULL && first->right!=NULL)
    //             q1.push(first->right);
    //         if(first==NULL && !q1.empty())
    //             q1.push(NULL);
    //     }
    // }

    // void rev(vector<TreeNode*>&v){
    //     int j=-1;
    //     for(int i=0;i<v.size();i++){
    //         if(v[i]==NULL && j==-1)
    //             j = i;
    //         else if(v[i]==NULL){
    //             reverse(v.begin()+j+1,v.begin()+i);
    //             j = i;
    //         }
    //     }
    // }

    // TreeNode* convTree(vector<TreeNode*>&v,int i,int n){
    //     TreeNode *root = NULL;
    //     if (i < n){
    //         root = new TreeNode(v[i]->val);
    //         // insert left child
    //         root->left = convTree(v,2 * i + 1, n);
  
    //         // insert right child
    //         root->right = convTree(v,2 * i + 2, n);
    //     }
    //     return root;
    // }

    // void rem(vector<TreeNode*>&v){
    //     for(int i=0;i<v.size();i++){
    //         if(v[i]==NULL)
    //             v.erase(v.begin()+i);
    //     }
    // }



    // TreeNode* invertTree(TreeNode* root) {
    //     if(root==NULL || root->left==NULL && root->right==NULL)
    //         return root;
    //     if(root->left == NULL){
    //         root->left = root->right;
    //         root->right = NULL;
    //         return root;
    //     }
    //     if(root->right == NULL){
    //         root->right = root->left;
    //         root->left = NULL;
    //         return root;
    //     }
    //     vector<TreeNode*> v1;
    //     vector<TreeNode*> v2;

    //     bfs(root->left,v1);
    //     bfs(root->right,v2);
    //     rev(v1);
    //     rev(v2);

    //     for(int i=0;i<v1.size();i++){
    //         if(v1[i]==NULL)
    //             cout<<" null ";
    //         else
    //             cout<<v1[i]->val;
    //     }
    //     cout<<endl;
    //     for(int i=0;i<v2.size();i++){
    //         if(v2[i]==NULL)
    //             cout<<" null ";
    //         else
    //             cout<<v2[i]->val;
    //     }

    //     rem(v1);
    //     rem(v2);
    //     root->left = convTree(v2,0,v2.size());
    //     root->right = convTree(v1,0,v1.size());
    //     return root;
        

    // }

    void reverse1(TreeNode*&root){
        if(root==NULL)
            return;
        
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        root->left = right;
        root->right = left;
        reverse1(root->left);
        reverse1(root->right);

    }

    TreeNode* invertTree(TreeNode* root){
        reverse1(root);
        return root;
    }
};