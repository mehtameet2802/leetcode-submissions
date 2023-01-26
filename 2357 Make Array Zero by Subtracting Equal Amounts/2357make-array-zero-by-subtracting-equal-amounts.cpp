class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        set<int> s;
        priority_queue<int,vector<int>,greater<int>> pq;
        priority_queue<int,vector<int>,greater<int>> pq1;
        for(int i=0;i<nums.size();i++){
            s.insert(nums[i]);
        }

        for(auto it:s){
            pq.push(it);
        }

        int count = 0;
        while(!pq.empty()){
            if(pq.top() == 0)
                pq.pop();
            
            int x = pq.top();
            while(!pq.empty()){
                int y = pq.top()-x;
                pq.pop();
                pq1.push(y);
            }

            while(!pq1.empty()){
                int y = pq1.top();
                pq1.pop();
                pq.push(y);
            }
            count++;
        }
        return count-1;
    }
};