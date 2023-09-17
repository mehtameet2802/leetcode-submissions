class Solution {
public:
    int largestRectangleArea(vector<int>& hei) {
        stack<pair<int,int>> st;
        int n = hei.size();
        vector<int> v(n,0);
        for(int i=0;i<n;i++){
            int cnt = 1;
            while(!st.empty() && hei[i]<=st.top().first){
                cnt+=st.top().second;
                st.pop();
            }
            st.push(make_pair(hei[i],cnt));
            v[i] = cnt;
        }

        st = stack<pair<int,int>>();
        for(int i=n-1;i>=0;i--){
            int cnt = 1;
            while(!st.empty() && hei[i]<=st.top().first){
                cnt+=st.top().second;
                st.pop();
            }
            st.push(make_pair(hei[i],cnt));
            v[i] = v[i]+cnt-1;
        }

        int ans = INT_MIN;
        for(int i=0;i<n;i++){
            v[i] = v[i]*hei[i];
            ans = max(ans,v[i]);
        }
        return ans;
    }
};