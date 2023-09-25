class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int k) {
         vector<int> v1;
        v1.push_back(nums[0]);
        int cnt=0;
        map<int,int> mp;
        mp[0] = 1;
        for(int i=1;i<nums.size();i++){
            v1.push_back(v1[i-1]+nums[i]);
        }
        
        for(int i=0;i<v1.size();i++){
            int z = v1[i]-k;
            if(mp.find(z)!=mp.end()){
                cnt+=mp[z];
            }
            mp[v1[i]]+=1;
        }
        return cnt;
    }
};