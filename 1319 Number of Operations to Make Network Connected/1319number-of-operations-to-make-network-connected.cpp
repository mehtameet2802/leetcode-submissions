class Solution {
public:

    void dfs(int cur,vector<int> mat[],vector<int> &vis){
        vis[cur] = 1;
        for(auto it:mat[cur]){
            if(vis[it]==0){
                vis[it] = 1;
                dfs(it,mat,vis);
            }
        }
    }

    int makeConnected(int n, vector<vector<int>>& connections) {
        int x = connections.size();
        if(x<n-1)
            return -1;
        vector<int> vis(n,0);

        vector<int> mat[n];
        for(int i=0;i<connections.size();i++){
            mat[connections[i][0]].push_back(connections[i][1]);
            mat[connections[i][1]].push_back(connections[i][0]);
        }

        int component = 0;
        for(int i=0;i<n;i++){
            if(vis[i]==0){
                dfs(i,mat,vis);
                component++;
            }       
        }

        int count = 0;
        for(auto it:vis){
            if(it == 1)
                count++;
        }
    
        int edges = connections.size();
        int redundant = edges-((n-1)-(component-1));
        if(redundant>=component-1)
            return component-1;
        return -1;
    }
};