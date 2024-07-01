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
    bool hasCycle(ListNode *head) {
        if(!head)
            return false;
        ListNode* slow = head->next;
        ListNode* fast = head;
        if(fast->next!=NULL && fast->next->next!=NULL){
            fast = fast->next->next;
        }
        else
            return false;
        while(fast!=NULL && fast->next!=NULL && slow!=fast){
            slow = slow->next;
            fast = fast->next->next;
        }
        if(slow==fast)
            return true;
        return false;
    }
};