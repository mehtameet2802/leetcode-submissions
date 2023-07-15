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
    int l1(ListNode* head){
        ListNode* temp=head;
        int len = 0;
        while(temp!=NULL){
            temp = temp->next;
            len++;
        }
        return len;
    }
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {

        if(headA==NULL || headB==NULL)
            return NULL;

        int c1 = l1(headA);
        int c2 = l1(headB);
        ListNode* temp1 = headA;
        ListNode* temp2 = headB;

        if(c1>c2){
            while(c1>c2){
                temp1 = temp1->next;
                c1--;
            }
        }
        else{
            while(c2>c1){
                temp2 = temp2->next;
                c2--;
            }
        }

        while(temp1 && temp2){
            if(temp1 == temp2)
                return temp1;
            temp1 = temp1->next;
            temp2 = temp2->next;
        }

        return NULL;
    }
};