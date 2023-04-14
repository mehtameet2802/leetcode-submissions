class Solution {
public:
    int m = 1000000000 + 7;
    int countWays(vector<vector<int>>& ranges) {
        sort(ranges.begin(),ranges.end());
        if(ranges.size()==1)
            return 2;
        vector<vector<int>> ans;
        vector<int> l = ranges[0];
        vector<int> r = ranges[1];
        int n = ranges.size();
        
        if(ranges.size() == 2){
            if(l[1]>=r[0] && l[1]<=r[1] || l[1]>=r[1])
                return 2;
            else
                return 4;
        }
        
        for(int i=2;i<=n;i++){
            if(l[1]>=r[0] && l[1]<=r[1]){
                l[1] = r[1];
                if(i<n)
                    r = ranges[i];
            }
            else if(l[1]>=r[1]){
                if(i<n)
                    r = ranges[i];
            }
            else{
                ans.push_back({l[0],l[1]});
                l = r;
                if(i<n)
                    r = ranges[i];
            }
        }
        ans.push_back({l[0],l[1]});
        int x = ans.size()%m;
        int a = 1;
        for(int i=0;i<x;i++){
            a = (a*2)%m;
        }
        return a;
    }
};