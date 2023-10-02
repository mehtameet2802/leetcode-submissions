/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string a1 = "";
        if(!root)
            return a1;
        queue<TreeNode*> q1;
        q1.push(root);
        while(!q1.empty()){
            TreeNode* f1 = q1.front();
            q1.pop();
            if(!f1)
                a1.append("#,");
            else{
                a1.append(to_string(f1->val)+',');
                q1.push(f1->left);
                q1.push(f1->right);
            }
        }
        return a1;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.size()==0)
            return NULL;
        
        stringstream s(data);
        string str;
        getline(s,str,',');

        queue<TreeNode*> q1;
        TreeNode* root = new TreeNode(stoi(str));
        q1.push(root);
        
        while(!q1.empty()){
            TreeNode* f1 = q1.front();
            q1.pop();
            
            getline(s,str,',');
            if(str=="#")
                f1->left = NULL;
            else{
                TreeNode* l = new TreeNode(stoi(str));
                f1->left = l;
                q1.push(l);
            }

            getline(s,str,',');
            if(str=="#")
                f1->right = NULL;
            else{
                TreeNode* r = new TreeNode(stoi(str));
                f1->right = r;
                q1.push(r);
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));