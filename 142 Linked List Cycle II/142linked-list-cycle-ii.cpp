/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(!head)
            return NULL;
        ListNode* slow = head->next;
        ListNode* fast = head;
        if(fast->next!=NULL && fast->next->next!=NULL){
            fast = fast->next->next;
        }
        else
            return NULL;
        
        while(fast!=NULL && fast->next!=NULL && slow!=fast){
            slow = slow->next;
            fast = fast->next->next;
        }
        if(slow==fast){
            fast = head;
        }
        else
            return NULL;

        while(slow!=fast){
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};