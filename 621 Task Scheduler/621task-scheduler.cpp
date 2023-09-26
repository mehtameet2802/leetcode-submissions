class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        if(n==0)
            return tasks.size();
        
        map<char,int> mp;
        for(char c:tasks)
            mp[c]++;

        priority_queue<int> pq;
        for(auto it:mp)
            pq.push(it.second);
        
        int ans = 0;
        while(!pq.empty()){
            int time = 0;
            vector<int> tmp;
            for(int i=0;i<n+1;i++){
                if(!pq.empty()){
                    tmp.push_back(pq.top()-1);
                    pq.pop();
                    time++;
                }
            }
            for(int i=0;i<tmp.size();i++){
                if(tmp[i]>0)
                    pq.push(tmp[i]);
            }
            ans+= pq.empty()?time:n+1;
        }
        return ans;
    }
};