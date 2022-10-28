class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int sum = 0;
        int longest = 0;
        unordered_map<int,int> mp;
        for(int i=0;i<nums.size();i++){
            
            if(nums[i] == 0)
                sum--;
            else
                sum++;
            
            if(sum == 0){
                longest = i+1;
            }
            else if(mp.find(sum)!=mp.end()){
                if(longest<(i-mp[sum])){
                    longest = i-mp[sum];
                }
            }
            else{
                mp[sum] = i;
            }
        }
        return longest;
    }
};