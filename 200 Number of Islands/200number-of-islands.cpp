class Solution {
public:

     void bfs(vector<vector<char>>&grid,vector<vector<int>> &vis,int n,int m,int c1,int c2){
        vector<int> x = {-1,0,0,1};
        vector<int> y = {0,1,-1,0};
        
        vis[c1][c2] = 1;
        queue<pair<int,int>> q1;
        q1.push(make_pair(c1,c2));
        
        while(!q1.empty()){
            pair<int,int> p1 = q1.front();
            q1.pop();
            int c1 = p1.first;
            int c2 = p1.second;
            vis[c1][c2] = 1;
            for(int i=0;i<4;i++){
                int x1 = c1+x[i];
                int y1 = c2+y[i];
                if(x1>=0 && x1<n && y1>=0 && y1<m && vis[x1][y1]==0 && grid[x1][y1]=='1'){
                    vis[x1][y1] = 1;
                    q1.push(make_pair(x1,y1));
                }
            }
        }
        
    }

    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> vis(n,vector<int>(m,0));
        int ans = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(vis[i][j]==0 && grid[i][j]=='1'){
                    bfs(grid,vis,n,m,i,j);
                    ans++;
                }
            }
        }
        return ans;
    }
};