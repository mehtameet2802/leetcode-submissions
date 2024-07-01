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
    bool isPalindrome(ListNode* head) {
        if(head->next==NULL)
            return true;
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev;
        while(fast!=NULL && fast->next!=NULL){
            fast = fast->next->next;
            prev = slow;
            slow = slow->next;
        }

        if(fast!=NULL)
            slow = slow->next;
                
        prev->next = NULL;
        ListNode* cur = head;
        ListNode* next;
        prev = NULL;
        while(cur!=NULL){
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        while(slow!=NULL && prev!=NULL && slow->val==prev->val){
            slow = slow->next;
            prev = prev->next;
        }

        if(slow==NULL && prev==NULL)
            return true;
        return false;

    }
};