class Solution {
public:
    int bfs(vector<vector<int>>& grid,int i,int j){
        int m = grid.size();
        int n = grid[0].size();
        int area = 0;
        queue<pair<int,int>> q;
        q.push({i,j});
        if(grid[i][j] == 1)
            grid[i][j] = -1;
        vector<int> v1 = {-1,0,1,0};
        vector<int> v2 = {0,-1,0,1};
        while(!q.empty()){
            int x = q.front().first;
            int y = q.front().second;
            if(grid[x][y] == -1)
                area++;
            q.pop();
            for(int k=0;k<4;k++){
                int x1 = x+v1[k];
                int y1 = y+v2[k];
                if(x1>=0 && x1<m && y1>=0 && y1<n &&  grid[x1][y1] == 1 && grid[x1][y1] != -1){
                    q.push({x1,y1});
                    grid[x1][y1] = -1;
                }
            }
        }
        return area;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int area = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1 && grid[i][j]!=-1){
                    int ans = bfs(grid,i,j);
                    area = max(area,ans);
                }
            }
        }
        return area;
    }
};