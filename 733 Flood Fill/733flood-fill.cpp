class Solution {
public:

    void solve(vector<vector<int>>& image, int sr, int sc,int initial, int color,int m,int n){
        queue<pair<int,int>> q1;
        q1.push({sr,sc});
        image[sr][sc] = color;

        vector<int> x = {1,0,-1,0};
        vector<int> y = {0,1,0,-1};

        while(!q1.empty()){
            pair<int,int> p1 = q1.front();
            q1.pop();
            int r = p1.first;
            int c = p1.second;
            for(int i=0;i<x.size();i++){
                int x1 = r+x[i];
                int y1 = c+y[i];
                if(x1>=0 && x1<m && y1>=0 && y1<n && image[x1][y1]==initial && image[x1][y1]!=color){
                    image[x1][y1] = color;
                    q1.push({x1,y1});
                }
            }
        }
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int m = image.size();
        int n = image[0].size();
        solve(image,sr,sc,image[sr][sc],color,m,n);
        return image;
    }
};