/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


int getDecimalValue(struct ListNode* head){
    struct ListNode* s= head;
    struct ListNode* p=NULL, *a;
    
    while(s!=NULL){
        a = s->next;
        s->next = p;
        p = s;
        s = a;
    }
        
    int sum = 0;
    int i=0;
    while(p){
        sum += (p->val)*pow(2,i);
        i++;
        p = p->next;
    }
    return sum;
}