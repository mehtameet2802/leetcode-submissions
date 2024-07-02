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
    
    void reverse(ListNode*& head, ListNode*&h1, ListNode*&p1, ListNode*&p2, int &count, ListNode* cur){
        ListNode* c1 = h1;
        ListNode* prev;
        ListNode* n1;
        while(c1!=cur){
            n1 = c1->next;
            c1->next = prev;
            prev = c1;
            c1 = n1;
        }
        count = 0;
        if(p1)
            p1->next = p2;
        else
            head = p2;
        p1 = h1;
        h1->next = cur;
        h1 = cur;
        count=0;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1)
            return head;
        
        ListNode* cur=head;
        ListNode* h1=head;
        ListNode* p1=NULL;
        ListNode* p2;
        int count = 0;

        while(cur!=NULL){
            if(count==k)
                reverse(head,h1,p1,p2,count,cur);
            p2 = cur;
            cur = cur->next;
            count++;
        }

        if(count==k)
            reverse(head,h1,p1,p2,count,cur);

        return head;
    }
};