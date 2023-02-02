/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    void bfs(Node*&root){
        Node *n = NULL;
        queue<Node*> q1;
        cout<<root->val;
        q1.push(root);
        q1.push(n);
        while(!q1.empty()){
            Node *first = q1.front();
            if(first == NULL){
                q1.pop();
                continue;
            }   
            q1.pop();
            first->next = q1.front();
            if(first->left != NULL)
                q1.push(first->left);
            if(first->right !=NULL)
                q1.push(first->right);
            if(!q1.empty() && q1.front() == NULL){
                q1.pop();
                q1.push(n);
            }
        }
    }

    Node* connect(Node* root) {
        if(root==NULL)
            return root;
        bfs(root);
        return root;
    }
};