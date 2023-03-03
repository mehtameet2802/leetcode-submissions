class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int g=0;
        int c=0;
        for(int i=0;i<gas.size();i++){
            g+=gas[i];
        }

        for(int i=0;i<cost.size();i++){
            c+=cost[i];
        }

        if(g<c)
            return -1;
        
        int cur = 0;
        int start=0;
        for(int i=0;i<gas.size();i++){
            cur+=(gas[i]-cost[i]);
            if(cur<0){
                start=i+1;
                cur=0;
            }
        }
        return start;
    }
};