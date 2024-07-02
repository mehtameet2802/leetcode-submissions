/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> mp1;
        Node* cur = head;
        while(cur){
            mp1[cur] = new Node(cur->val);
            cur = cur->next;
        }

        cur = head;
        while(cur){
            mp1[cur]->next = mp1[cur->next];
            mp1[cur]->random = mp1[cur->random];
            cur = cur->next;
        }

        return mp1[head];
    }
};