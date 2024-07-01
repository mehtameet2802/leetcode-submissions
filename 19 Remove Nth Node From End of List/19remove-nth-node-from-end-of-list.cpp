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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* cur=head;
        ListNode* prev;
        int count = 0;
        while(cur!=NULL){
            cur = cur->next;
            count++;
        }
        n = count-n;
        cur = head;

        if(n==0){
            cur = head;
            head = head->next;
            delete cur;
            return head;
        }

        while(n!=0){
            prev = cur;
            cur = cur->next;
            n--;
        }
        cout<<count;
        prev->next = cur->next;
        delete cur;
        return head;
    }
};