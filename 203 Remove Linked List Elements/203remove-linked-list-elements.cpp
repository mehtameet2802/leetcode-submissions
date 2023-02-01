/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val1) {
        int n = 0;
        int x = 0;
        ListNode*temp = head;
        ListNode*prev = temp;
        
        while(temp!=NULL){
            if(temp->val == val1)
                x++;
            temp = temp->next;
            n++;
        }

        if(n == 0 || n == x)
            return NULL;
    
        temp = head;
        prev = NULL;
        while(temp!=NULL){
            if(temp->val == val1){
                if(temp == head)
                    head = head->next;
                else{
                    prev->next = temp->next;
                    temp = temp->next;
                    continue;
                }
            }
            prev = temp;
            temp = temp->next;
        }
        return head;  
    }
};