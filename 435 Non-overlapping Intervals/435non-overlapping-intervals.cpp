class Solution {
public:

    int eraseOverlapIntervals(vector<vector<int>>& inter) {
        int n = inter.size();
        sort(inter.begin(),inter.end());
        int count = 0;
        int l = 0;
        int r = 1;
        while(r<n){
            if(inter[l][1]<=inter[r][0]){
                l = r;
                r++;
            }
            else if(inter[l][1]<=inter[r][1]){
                r++;
                count++;
            }
            else if(inter[l][1]>inter[r][1]){
                l=r;
                count++;
                r++;
            }
        }
        return count;
    }
};