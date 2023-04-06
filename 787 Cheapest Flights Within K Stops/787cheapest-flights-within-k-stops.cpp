class Solution {
public:

    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<pair<int,int>> adj[n];
        for(auto it:flights){
            adj[it[0]].push_back({it[1],it[2]});
        }
        
        vector<int> dist(n,INT_MAX);
        queue<pair<int,pair<int,int>>> q1;
        q1.push(make_pair(0,make_pair(src,0)));
        vector<int> vis(n,0);
        dist[src] = 0;

        while(!q1.empty()){
            auto it = q1.front();
            q1.pop();
            int stop = it.first;
            int node = it.second.first;
            int d = it.second.second;
            if(stop>k)
                continue;
            for(auto it1:adj[node]){
                if(dist[it1.first]>d+it1.second && stop<=k){
                    q1.push({stop+1,{it1.first,d+it1.second}});
                    dist[it1.first] = d+it1.second;
                }
                    
            }
        }

        if(dist[dst] == INT_MAX)
            return -1;
        return dist[dst];
    }
};