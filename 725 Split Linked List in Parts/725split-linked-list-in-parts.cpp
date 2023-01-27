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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n=0;
        ListNode* temp = head;
        while(temp!=NULL){
            temp = temp->next;
            n++;
        }
        temp = head;
        int i=n/k;
        int j=n%k;
        int t = k-j;
        vector<ListNode*> ans;
        while(j!=0){
            ans.push_back(temp);
            int t = i+1;
            ListNode* prev = temp;
            while(t!=0 && temp!=NULL){
                prev = temp;
                temp = temp->next;
                t--;
            }
            if(prev!=NULL)
                prev->next = NULL;
            j--;
        }
        while(t!=0){
            ans.push_back(temp);
            int y = i;
            ListNode* prev = temp;
            while(y!=0 && temp!=NULL){
                prev = temp;
                temp = temp->next;
                y--;
            }
            if(prev!=NULL)
                prev->next = NULL;
            t--;
        }
        return ans;
    }
};