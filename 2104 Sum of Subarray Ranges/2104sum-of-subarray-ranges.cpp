class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        vector<long long> v1(n,1);
        vector<long long> v2(n,1);
        vector<long long> v3(n,1);
        vector<long long> v4(n,1);
        stack<pair<int,int>> st1;
        stack<pair<int,int>> st2;
        stack<pair<int,int>> st3;
        stack<pair<int,int>> st4;
        for(int i=0;i<nums.size();i++){
            int cnt = 1;
            while(!st1.empty() && st1.top().first>=nums[i]){
                cnt += st1.top().second;
                st1.pop();
            }
            st1.push(make_pair(nums[i],cnt));
            v1[i] = cnt;

            cnt = 1;
            while(!st3.empty() && st3.top().first<=nums[i]){
                cnt += st3.top().second;
                st3.pop();
            }
            st3.push(make_pair(nums[i],cnt));
            v3[i] = cnt;
        }

        for(int i=n-1;i>=0;i--){
            int cnt = 1;
            while(!st2.empty() && st2.top().first>nums[i]){
                cnt += st2.top().second;
                st2.pop();
            }
            st2.push(make_pair(nums[i],cnt));
            v2[i] = cnt;

            cnt = 1;
            while(!st4.empty() && st4.top().first<nums[i]){
                cnt += st4.top().second;
                st4.pop();
            }
            st4.push(make_pair(nums[i],cnt));
            v4[i] = cnt;
        }

        for(int i=0;i<n;i++){
            ans += nums[i]*((v4[i]*v3[i]) - (v1[i]*v2[i]));
        }
        return ans;
    }
};