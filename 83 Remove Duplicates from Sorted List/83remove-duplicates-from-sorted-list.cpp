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
    ListNode* deleteDuplicates(ListNode* head) {
        map<int,int> mp;
        ListNode * temp = head;
        while(temp!=NULL){
            mp[temp->val]++;
            temp = temp->next;
        }
        int x = mp.size();
        if(x == 0)
            return head;
        head = NULL;
        x = 1;
        for(auto it:mp){
            ListNode* n = new ListNode(it.first);
            if(x == 1){
                x--;
                head = n;
                temp = head;
            }
            else{
                temp->next = n;
                temp = temp->next;
            }
        }
        return head;
    }
};