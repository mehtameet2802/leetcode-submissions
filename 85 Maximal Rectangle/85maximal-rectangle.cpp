class Solution {
public:

    int solve(vector<int> v1){
        stack<pair<int,int>> st;
        int n = v1.size();
        vector<int> v(n,0);
        for(int i=0;i<n;i++){
            int cnt = 1;
            while(!st.empty() && v1[i]<=st.top().first){
                cnt+=st.top().second;
                st.pop();
            }
            st.push(make_pair(v1[i],cnt));
            v[i] = cnt;
        }

        st = stack<pair<int,int>>();
        for(int i=n-1;i>=0;i--){
            int cnt = 1;
            while(!st.empty() && v1[i]<=st.top().first){
                cnt+=st.top().second;
                st.pop();
            }
            st.push(make_pair(v1[i],cnt));
            v[i] = v[i]+cnt-1;
        }

        int ans = INT_MIN;
        for(int i=0;i<n;i++){
            v[i] = v[i]*v1[i];
            ans = max(ans,v[i]);
        }
        return ans;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        if(m==n && m==1)
            return matrix[0][0]-'0';

        int ans = INT_MIN;
        vector<int> v1(n,0);
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]-'0' == 0)
                    v1[j] = 0;
                else
                    v1[j] = v1[j]+matrix[i][j]-'0';
            }
            ans = max(ans,solve(v1));
        }       
        return ans;     
    }
};