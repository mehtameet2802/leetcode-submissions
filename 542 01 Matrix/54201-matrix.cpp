// class Solution {
// public:
//     int bfs(int x,int y,vector<vector<int>>& mat){
//         int m = mat.size();
//         int n = mat[0].size();
//         int dist = 0;
//         vector<int> v1 = {1,0,-1,0};
//         vector<int> v2 = {0,-1,0,1};
//         queue<pair<int,pair<int,int>>> q1;
//         int i = x;
//         int j = y;
//         q1.push({0,{i,j}});
//         while(!q1.empty()){
//             int i1 = q1.front().second.first;
//             int j1 = q1.front().second.second;
//             int d = q1.front().first;
//             dist = max(dist,d);
//             if(mat[i1][j1] == 0)
//                 break;
//             q1.pop();
//             for(int k=0;k<4;k++){
//                 int i2 = i1+v1[k];
//                 int j2 = j1+v2[k];
//                 if(i2>=0 && i2<m && j2>=0 && j2<n){
//                     q1.push({d+1,{i2,j2}});
//                 }
//             }
//         }
//         return dist;
//     }
//     vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
//         int m = mat.size();
//         int n = mat[0].size();
//         int zero = 0;
//         int count = 0;        
//         queue<pair<int,int>> q1;
//         for(int i=0;i<m;i++){
//             for(int j=0;j<n;j++){
//                 if(mat[i][j] == 1)
//                     q1.push({i,j});
//                 else if(mat[i][j] == 0)
//                     zero++;
//             }
//         }

//         if(q1.size() == 0)
//             return mat;
        
//         vector<vector<int>> ans(m,vector<int>(n,0));

//         while(!q1.empty()){
//             int d = bfs(q1.front().first,q1.front().second,mat);
//             ans[q1.front().first][q1.front().second] = d;
//             q1.pop();
//         }

//         return ans;
//     }
// };

class Solution {
public:
    vector<int> DIR = {0, 1, 0, -1, 0};
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        queue<pair<int, int>> q;
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                if (mat[r][c] == 0) q.emplace(r, c);
                else mat[r][c] = -1; // Marked as not processed yet!

        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();
            for (int i = 0; i < 4; ++i) {
                int nr = r + DIR[i], nc = c + DIR[i+1];
                if (nr < 0 || nr == m || nc < 0 || nc == n || mat[nr][nc] != -1) continue;
                mat[nr][nc] = mat[r][c] + 1;
                q.emplace(nr, nc);
            }
        }
        return mat;
    }
};
