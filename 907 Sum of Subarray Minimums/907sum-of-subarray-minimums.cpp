class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        stack<pair<int,int>> st;
        stack<pair<int,int>> st1;
        long long int k = pow(10,9)+7;
        int n = arr.size();
        vector<int> left(n,1);
        vector<int> right(n,1);
        for(int i=0;i<n;i++){
            int cnt = 1;
            while(!st.empty() && arr[i]<st.top().first){
                cnt += st.top().second%k;
                st.pop();
            }
            st.push(make_pair(arr[i],cnt));
            left[i] = cnt%k;
        }

        for(int i=n-1;i>=0;i--){
            int cnt = 1;
            while(!st1.empty() && arr[i]<=st1.top().first){
                cnt += st1.top().second%k;
                st1.pop();
            }
            st1.push(make_pair(arr[i],cnt));
            right[i] = cnt%k;
        }

        
        int ans = 0;
        for(int i=0;i<n;i++){
            ans = (ans%k + (left[i]%k)*(right[i]%k)*arr[i]%k)%k;
        }
        return ans;
    }
};