class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int fresh = 0;
        int count = 0;        
        queue<pair<int,pair<int,int>>> q1;
        int ans = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] == 2)
                    q1.push({0,{i,j}});
                else if(grid[i][j] == 1)
                    fresh++;
            }
        }

        if(q1.size() == 0 && fresh!=0)
            return -1;
        if(q1.size() == 0)
            return 0;
        
        vector<int> v1 = {1,0,-1,0};
        vector<int> v2 = {0,-1,0,1};
        while(!q1.empty()){
            int i1 = q1.front().second.first;
            int j1 = q1.front().second.second;
            int t = q1.front().first;
            count = max(count,t);
            q1.pop();
            for(int k=0;k<4;k++){
                int i2 = i1+v1[k];
                int j2 = j1+v2[k];
                if(i2>=0 && i2<m && j2>=0 && j2<n && grid[i2][j2]==1 && fresh!=0){
                    q1.push({t+1,{i2,j2}});
                    fresh--;
                    grid[i2][j2] = 2;
                }
            }
        }

        if(fresh!=0)
            return -1;

        return count;
    }
};