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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int count = 1;
        if(left == right){
            return head;
        }
        ListNode * temp = head;
        ListNode * prev1 = temp;
        while(temp!=NULL && count!=left){
            count++;
            prev1 = temp;
            temp = temp->next;
        }
        cout<<count;
        if(temp == NULL){
            return head;
        }
        ListNode * start = temp;
        ListNode * prev = NULL;
        ListNode * ahead = NULL;
        while(count!=right+1){
            count++;
            ahead = start->next;
            start->next = prev;
            prev = start;
            start = ahead;
        }
        if(temp == head){
            head = prev;
        }
        else{
            prev1->next = prev;
        }
        temp->next = ahead;
        return head;
    }
};