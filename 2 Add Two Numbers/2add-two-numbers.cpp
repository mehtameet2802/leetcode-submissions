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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode();
        ListNode* cur = head;
        int c1=0;
        while(l1!=NULL && l2!=NULL){
            int a1 = l1->val+l2->val+c1;
            int a2 = a1%10;
            cur->next = new ListNode(a2);
            c1 = a1/10;
            l1 = l1->next;
            l2 = l2->next;
            cur = cur->next;
        }

        while(l1!=NULL){
            int a1 = l1->val+c1;
            int a2 = a1%10;
            cur->next = new ListNode(a2);
            c1 = a1/10;
            l1 = l1->next;
            cur = cur->next;
        }

        while(l2!=NULL){
            int a1 = l2->val+c1;
            int a2 = a1%10;
            cur->next = new ListNode(a2);
            c1 = a1/10;
            l2 = l2->next;
            cur = cur->next;
        }

        if(c1!=0)
            cur->next = new ListNode(c1);
        return head->next;

    }
};