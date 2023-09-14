class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> l;
        vector<int> r(n,0);
        l.push_back(height[0]);
        for(int i=1;i<height.size();i++){
            l.push_back(max(l[i-1],height[i]));
        }
        r[n-1] = height[n-1];
        for(int i=n-2;i>=0;i--){
            r[i] = max(r[i+1],height[i]);
        }

        int ans = 0;
        for(int i=0;i<n;i++){
            ans += min(l[i],r[i])-height[i];
        }
        return ans;
    }
};