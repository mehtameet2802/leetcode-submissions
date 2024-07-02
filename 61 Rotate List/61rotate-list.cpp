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
    ListNode* rotateRight(ListNode* head, int k) {
        if(k==0)
            return head;
        int count = 0;
        ListNode* cur = head;
        while(cur!=NULL){
            count++;
            cur = cur->next;
        }
        if(count==0)
            return head;
        k = k%count;
        k = count-k;
        if(k==count)
            return head;
        ListNode* prev;
        cur = head;
        while(k!=0){
            prev = cur;
            cur=cur->next;
            k--;
        }
        ListNode* h1 = head;
        prev->next = NULL;
        head = cur;
        while(cur!=NULL){
            prev=cur;
            cur = cur->next;
        }
        prev->next = h1;
        return head;
    }
};